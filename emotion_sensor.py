import cv2
import datetime
from deepface import DeepFace
from pymongo import MongoClient

class EmotionSensor:
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
    
    def save_to_database(self, emotion):
        """Save emotion data to MongoDB"""
        try:
            data = {
                "sensor_type": "emotion",
                "value": emotion,
                "timestamp": datetime.datetime.now(),
                "operator_name": self.operator_name
            }
            self.collection.insert_one(data)
            print(f"Saved to DB: {emotion} at {data['timestamp']}")
        except Exception as e:
            print(f"Failed to save to database: {e}")
    
    def detect_emotion(self, frame):
        """Detect emotion from frame"""
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
                
                # Draw rectangle and label
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                
                # Save to database
                self.save_to_database(emotion)
                
                return emotion
            
            return None
        except Exception as e:
            print(f"Error in emotion detection: {e}")
            return None
    
    def run(self):
        """Main execution loop"""
        print("=== Emotion Detection Sensor ===")
        
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
        
        print("Starting emotion detection... Press ESC to stop")
        
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("Failed to capture frame")
                    break
                
                # Detect emotion
                emotion = self.detect_emotion(frame)
                
                # Display frame
                cv2.imshow('Emotion Detection Sensor', frame)
                
                # Check for exit
                if cv2.waitKey(1) == 27:  # ESC key
                    break
                    
        except KeyboardInterrupt:
            print("\nStopping emotion detection...")
        
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
        if self.db_client:
            self.db_client.close()
        print("Emotion sensor stopped and cleaned up")

if __name__ == "__main__":
    sensor = EmotionSensor()
    sensor.run()