import cv2
import datetime
from deepface import DeepFace
from pymongo import MongoClient

class StressSensor:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.cap = None
        self.operator_name = ""
        self.db_client = None
        self.collection = None
        
    def connect_database(self):
        """Connect to MongoDB database"""
        try:
            self.db_client = MongoClient('mongodb://localhost:27017/')
            db = self.db_client['sensor_data']
            self.collection = db['readings']
            print("Connected to MongoDB successfully")
            return True
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            return False
    
    def initialize_camera(self):
        """Initialize camera capture"""
        try:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                print("Error: Could not open camera")
                return False
            print("Camera initialized successfully")
            return True
        except Exception as e:
            print(f"Failed to initialize camera: {e}")
            return False
    
    def classify_stress_level(self, emotion):
        """Classify stress level based on detected emotion"""
        emotion_lower = emotion.lower()
        
        if emotion_lower in ["angry", "fear", "sad"]:
            return "high stress"
        elif emotion_lower in ["disgust", "surprise"]:
            return "low stress"
        else:
            return "no stress"
    
    def save_to_database(self, stress_level):
        """Save stress data to MongoDB"""
        try:
            data = {
                "sensor_type": "stress",
                "value": stress_level,
                "timestamp": datetime.datetime.now(),
                "operator_name": self.operator_name
            }
            self.collection.insert_one(data)
            print(f"Saved to DB: {stress_level} at {data['timestamp']}")
        except Exception as e:
            print(f"Failed to save to database: {e}")
    
    def detect_stress(self, frame):
        """Detect stress level from frame"""
        try:
            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Convert grayscale to RGB for DeepFace
            rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)
            
            # Detect faces
            faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            for (x, y, w, h) in faces:
                # Extract face ROI
                face_roi = rgb_frame[y:y + h, x:x + w]
                
                # Perform emotion analysis
                result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
                emotion = result[0]['dominant_emotion']
                
                # Classify stress level
                stress_level = self.classify_stress_level(emotion)
                
                # Draw rectangle and label
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, f"{emotion} -> {stress_level}", (x, y - 10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
                # Display additional info
                cv2.putText(frame, f"Emotion: {emotion}", (10, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                cv2.putText(frame, f"Stress: {stress_level}", (10, 60),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                
                # Save to database
                self.save_to_database(stress_level)
                
                return stress_level
            
            return None
        except Exception as e:
            print(f"Error in stress detection: {e}")
            return None
    
    def run(self):
        """Main execution loop"""
        print("=== Stress Detection Sensor ===")
        
        # Get operator name
        self.operator_name = input("Please enter your name before starting: ")
        
        # Connect to database
        if not self.connect_database():
            print("Cannot proceed without database connection")
            return
        
        # Initialize camera
        if not self.initialize_camera():
            print("Cannot proceed without camera")
            return
        
        print("Starting stress detection... Press ESC to stop")
        
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("Failed to capture frame")
                    break
                
                # Detect stress
                stress_level = self.detect_stress(frame)
                
                # Display frame
                cv2.imshow('Stress Detection Sensor', frame)
                
                # Check for exit
                if cv2.waitKey(1) == 27:  # ESC key
                    break
                    
        except KeyboardInterrupt:
            print("\nStopping stress detection...")
        
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
        if self.db_client:
            self.db_client.close()
        print("Stress sensor stopped and cleaned up")

if __name__ == "__main__":
    sensor = StressSensor()
    sensor.run()