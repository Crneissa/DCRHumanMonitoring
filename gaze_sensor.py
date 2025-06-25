import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist
import datetime
from pymongo import MongoClient
import os

class GazeSensor:
    def __init__(self):
        self.detector = None
        self.predictor = None
        self.cap = None
        self.operator_name = ""
        self.db_client = None
        self.collection = None
        
        # Eye landmark indices for dlib's 68-point model
        self.left_eye_start, self.left_eye_end = 36, 42
        self.right_eye_start, self.right_eye_end = 42, 48
        
        # Blink detection parameters
        self.eye_ar_thresh = 0.2
        self.eye_ar_consec_frames = 3
        self.blink_counter = 0
        self.total_blinks = 0
        
        # Variables for alarm when eyes remain closed
        self.blink_start_time = None
        self.alarm_triggered = False
        
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
    
    def initialize_dlib(self):
        """Initialize dlib face detector and landmark predictor"""
        try:
            self.detector = dlib.get_frontal_face_detector()
            
            # Check if landmark file exists
            landmark_file = "shape_predictor_68_face_landmarks.dat"
            if not os.path.exists(landmark_file):
                print(f"Error: {landmark_file} not found!")
                print("Please download it from: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2")
                print("Extract the .bz2 file to get the .dat file")
                return False
                
            self.predictor = dlib.shape_predictor(landmark_file)
            print("Dlib initialized successfully")
            return True
        except Exception as e:
            print(f"Failed to initialize dlib: {e}")
            return False
    
    def eye_aspect_ratio(self, eye):
        """Compute the eye aspect ratio (EAR) to determine eye closure"""
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear
    
    def get_gaze_direction(self, eye_roi):
        """Determine gaze direction from eye region"""
        try:
            gray_eye = cv2.cvtColor(eye_roi, cv2.COLOR_BGR2GRAY)
            _, thresh_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
            
            h, w = thresh_eye.shape
            left_side = thresh_eye[0:h, 0:int(w/2)]
            right_side = thresh_eye[0:h, int(w/2):w]
            
            left_white = cv2.countNonZero(left_side)
            right_white = cv2.countNonZero(right_side)
            
            # Avoid division by zero
            if left_white == 0:
                gaze_ratio = 1
            else:
                gaze_ratio = right_white / left_white
            
            if gaze_ratio < 0.8:
                return "RIGHT"
            elif gaze_ratio > 1.2:
                return "LEFT"
            else:
                return "CENTER"
        except:
            return "CENTER"
    
    def save_to_database(self, state):
        """Save gaze data to MongoDB"""
        try:
            data = {
                "sensor_type": "gaze",
                "value": state,
                "timestamp": datetime.datetime.now(),
                "operator_name": self.operator_name
            }
            self.collection.insert_one(data)
            print(f"Saved to DB: {state} at {data['timestamp']}")
        except Exception as e:
            print(f"Failed to save to database: {e}")
    
    def detect_gaze_and_blinks(self, frame):
        """Detect gaze direction and blinks from frame"""
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.detector(gray, 0)
            
            for face in faces:
                # Detect facial landmarks
                shape = self.predictor(gray, face)
                shape_np = np.zeros((68, 2), dtype="int")
                for i in range(68):
                    shape_np[i] = (shape.part(i).x, shape.part(i).y)
                
                # Extract eye regions
                left_eye = shape_np[self.left_eye_start:self.left_eye_end]
                right_eye = shape_np[self.right_eye_start:self.right_eye_end]
                
                # Compute EAR for both eyes
                left_ear = self.eye_aspect_ratio(left_eye)
                right_ear = self.eye_aspect_ratio(right_eye)
                ear = (left_ear + right_ear) / 2.0
                
                # Blink detection
                if ear < self.eye_ar_thresh:
                    self.blink_counter += 1
                else:
                    if self.blink_counter >= self.eye_ar_consec_frames:
                        self.total_blinks += 1
                    self.blink_counter = 0
                
                # Check for prolonged eye closure
                if ear < self.eye_ar_thresh:
                    if self.blink_start_time is None:
                        self.blink_start_time = datetime.datetime.now()
                    else:
                        elapsed = (datetime.datetime.now() - self.blink_start_time).total_seconds()
                        if elapsed >= 3 and not self.alarm_triggered:
                            self.alarm_triggered = True
                            cv2.putText(frame, "ALERT: Eyes closed > 3 sec!", (10, 90),
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                else:
                    self.blink_start_time = None
                    self.alarm_triggered = False
                
                # Gaze direction estimation
                (l_x, l_y, l_w, l_h) = cv2.boundingRect(left_eye)
                left_eye_roi = frame[l_y:l_y+l_h, l_x:l_x+l_w]
                
                (r_x, r_y, r_w, r_h) = cv2.boundingRect(right_eye)
                right_eye_roi = frame[r_y:r_y+r_h, r_x:r_x+r_w]
                
                left_gaze = self.get_gaze_direction(left_eye_roi)
                right_gaze = self.get_gaze_direction(right_eye_roi)
                
                if left_gaze == right_gaze:
                    gaze_direction = left_gaze
                else:
                    gaze_direction = "CENTER"
                
                # Determine current state
                if ear < self.eye_ar_thresh:
                    current_state = "Blinking"
                else:
                    current_state = gaze_direction
                
                # Draw eye contours and landmarks
                left_eye_hull = cv2.convexHull(left_eye)
                right_eye_hull = cv2.convexHull(right_eye)
                cv2.drawContours(frame, [left_eye_hull], -1, (0, 255, 0), 2)
                cv2.drawContours(frame, [right_eye_hull], -1, (0, 255, 0), 2)
                
                # Draw landmarks
                for (x, y) in left_eye:
                    cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)
                for (x, y) in right_eye:
                    cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)
                
                # Display information
                cv2.putText(frame, f"State: {current_state}", (10, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                cv2.putText(frame, f"Blinks: {self.total_blinks}", (10, 60),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                
                # Save to database
                self.save_to_database(current_state)
                
                return current_state
            
            return None
        except Exception as e:
            print(f"Error in gaze detection: {e}")
            return None
    
    def run(self):
        """Main execution loop"""
        print("=== Gaze Tracking Sensor ===")
        
        # Get operator name
        self.operator_name = input("Please enter your name before starting: ")
        
        # Connect to database
        if not self.connect_database():
            print("Cannot proceed without database connection")
            return
        
        # Initialize dlib
        if not self.initialize_dlib():
            print("Cannot proceed without dlib initialization")
            return
        
        # Initialize camera
        if not self.initialize_camera():
            print("Cannot proceed without camera")
            return
        
        print("Starting gaze tracking... Press Q to stop")
        
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("Failed to capture frame")
                    break
                
                # Resize for faster processing
                frame = cv2.resize(frame, None, fx=0.8, fy=0.8)
                
                # Detect gaze and blinks
                state = self.detect_gaze_and_blinks(frame)
                
                # Display frame
                cv2.imshow('Gaze Tracking Sensor', frame)
                
                # Check for exit
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
                    
        except KeyboardInterrupt:
            print("\nStopping gaze tracking...")
        
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
        if self.db_client:
            self.db_client.close()
        print("Gaze sensor stopped and cleaned up")

if __name__ == "__main__":
    sensor = GazeSensor()
    sensor.run()