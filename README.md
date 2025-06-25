# Sensor Data Dashboard - POC

A real-time dashboard for monitoring emotion detection, gaze tracking, and stress detection sensors. This is a proof-of-concept system that captures sensor data in real-time and displays it on a web dashboard.

## System Architecture

```
Sensor Apps (Python) → MongoDB → Backend (Node.js + Socket.io) → Frontend (React + Socket.io)
```

## Components

1. **Sensor Apps** (Python): Three sensor applications that capture data from camera
   - `emotion_sensor.py` - Detects facial emotions
   - `gaze_sensor.py` - Tracks eye movement and blinks
   - `stress_sensor.py` - Monitors stress levels based on emotions

2. **Backend** (`server.js`): Node.js server with Express and Socket.io for real-time data streaming

3. **Frontend** (`index.html`): React-based dashboard with three panels showing sensor data in real-time

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- MongoDB Community Server
- Webcam/Camera
- Internet connection (for downloading models)

## Installation

### 1. Clone or Download the Project

Create a new directory and place all the project files:

```bash
mkdir sensor-dashboard
cd sensor-dashboard
```

### 2. Install MongoDB

**Windows:**
1. Download MongoDB Community Server from https://www.mongodb.com/try/download/community
2. Install with default settings
3. Start MongoDB service

**macOS:**
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb/brew/mongodb-community
```

**Linux (Ubuntu):**
```bash
sudo apt-get install gnupg
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Note:** If you encounter issues with dlib installation:

**Windows:**
```bash
pip install cmake
pip install dlib
```

**macOS:**
```bash
brew install cmake
pip install dlib
```

**Linux:**
```bash
sudo apt-get install build-essential cmake
sudo apt-get install libopenblas-dev liblapack-dev
pip install dlib
```

### 4. Download Required Models

**For Gaze Tracking (dlib facial landmarks):**
```bash
# Download the facial landmarks model
wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
# Extract the file
bunzip2 shape_predictor_68_face_landmarks.dat.bz2
```

Or manually:
1. Go to http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
2. Download and extract the .bz2 file
3. Place `shape_predictor_68_face_landmarks.dat` in the project root directory

### 5. Install Node.js Dependencies

```bash
npm install
```

## Running the System

### Step 1: Start MongoDB
Make sure MongoDB is running:

**Windows/macOS/Linux:**
```bash
# Check if MongoDB is running
mongosh --eval "db.adminCommand('ismaster')"
```

If not running, start it:
- **Windows:** Start from Services or run `net start MongoDB`
- **macOS:** `brew services start mongodb/brew/mongodb-community`
- **Linux:** `sudo systemctl start mongod`

### Step 2: Start the Backend Server

```bash
npm start
```

You should see:
```
=== Sensor Data Server ===
Server running on http://localhost:3000
Database: Connected
=========================
```

### Step 3: Open the Frontend Dashboard

Open your web browser and go to: http://localhost:3000

You should see the dashboard with three panels (all showing "Disconnected" initially).

### Step 4: Run Sensor Apps (One at a Time)

Open a new terminal for each sensor you want to run:

**Emotion Detection:**
```bash
python emotion_sensor.py
```

**Gaze Tracking:**
```bash
python gaze_sensor.py
```

**Stress Detection:**
```bash
python stress_sensor.py
```

## Usage Instructions

1. **Start the system** in the order: MongoDB → Backend → Frontend → Sensor Apps
2. **Run one sensor at a time** since they all use the same camera
3. **Enter your name** when prompted by each sensor
4. **Position yourself** in front of the camera with good lighting
5. **Watch the dashboard** update in real-time as the sensor detects data
6. **Stop sensors** by pressing the specified key (ESC for emotion/stress, Q for gaze)

## Controls

- **Emotion Sensor:** Press `ESC` to stop
- **Gaze Sensor:** Press `Q` to stop  
- **Stress Sensor:** Press `ESC` to stop
- **Backend:** Press `Ctrl+C` to stop

## Troubleshooting

### Camera Issues
```bash
# If camera fails to open, try different indices
# Edit the sensor files and change cv2.VideoCapture(0) to cv2.VideoCapture(1)
```

### MongoDB Connection Issues
```bash
# Check if MongoDB is running
mongosh

# If connection fails, restart MongoDB service
```

**Note:** This POC uses database polling instead of MongoDB Change Streams for simplicity. Change Streams require MongoDB to be configured as a replica set, which is unnecessary for a POC. The polling approach checks for new data every 500ms, providing near real-time updates while working with any MongoDB installation.

### Python Dependencies Issues
```bash
# Create a virtual environment (recommended)
python -m venv sensor-env
source sensor-env/bin/activate  # On Windows: sensor-env\Scripts\activate
pip install -r requirements.txt
```

### Node.js Dependencies Issues
```bash
# Clear npm cache and reinstall
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

### dlib Installation Issues

**If dlib fails to install:**

1. **Install Visual Studio Build Tools** (Windows only):
   - Download from https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Install C++ build tools

2. **Use conda instead of pip:**
   ```bash
   conda install -c conda-forge dlib
   ```

3. **Install pre-compiled wheels:**
   ```bash
   pip install https://github.com/sachadee/Dlib/raw/master/dlib-19.22.99-cp39-cp39-win_amd64.whl
   ```

## File Structure

```
sensor-dashboard/
├── emotion_sensor.py          # Emotion detection sensor
├── gaze_sensor.py             # Gaze tracking sensor  
├── stress_sensor.py           # Stress detection sensor
├── server.js                  # Backend server
├── index.html                 # Frontend dashboard
├── package.json               # Node.js dependencies
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── shape_predictor_68_face_landmarks.dat  # dlib model (download required)
```

## Features

### Sensor Capabilities
- **Emotion Detection:** Detects 7 emotions (happy, sad, angry, fear, surprise, disgust, neutral)
- **Gaze Tracking:** Tracks eye direction (LEFT, RIGHT, CENTER) and detects blinking
- **Stress Detection:** Classifies stress levels (high stress, low stress, no stress) based on emotions

### Dashboard Features
- **Real-time Updates:** Data streams instantly from sensors to dashboard
- **Connection Status:** Shows if each sensor is connected and active
- **Timestamp Display:** Shows when each sensor last sent data
- **Operator Tracking:** Displays who is currently using each sensor
- **Responsive Design:** Works on desktop and mobile browsers

## Technical Details

### Data Flow
1. Sensor apps capture camera frames and process them
2. Detected data is inserted into MongoDB in real-time
3. Backend polls the database every 500ms for new data (instead of Change Streams for POC simplicity)
4. New data is broadcasted to frontend via Socket.io
5. Frontend updates panels instantly when new data arrives

### Database Schema
```javascript
{
  sensor_type: "emotion" | "gaze" | "stress",
  value: "detected_value",
  timestamp: ISODate,
  operator_name: "user_name"
}
```

### API Endpoints
- `GET /` - Frontend dashboard
- `GET /health` - Server health check
- `GET /api/latest` - Get latest sensor data
- `GET /api/history/:sensorType` - Get sensor history

## Customization

### Modifying Sensor Sensitivity
Edit the sensor files to adjust detection parameters:

**Emotion Sensor:** Modify DeepFace confidence thresholds
**Gaze Sensor:** Adjust `eye_ar_thresh` for blink sensitivity
**Stress Sensor:** Modify emotion-to-stress mapping

### Changing Update Frequency
Sensors update on every frame detection. To reduce frequency, add delays in the sensor loops.

### Styling the Dashboard
Edit the TailwindCSS classes in `index.html` to customize the appearance.

## Known Limitations

1. **Single Camera:** Only one sensor can use the camera at a time
2. **Lighting Dependency:** Face detection requires good lighting conditions
3. **Performance:** Real-time processing is CPU intensive
4. **Model Accuracy:** Detection accuracy depends on camera quality and positioning

## Future Improvements

- Multi-camera support for concurrent sensors
- Data analytics and historical trends
- Alert system for specific conditions
- Mobile app for remote monitoring
- Machine learning model fine-tuning

## Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Verify all dependencies are installed correctly
3. Ensure MongoDB is running and accessible
4. Check camera permissions and availability
5. Review console outputs for error messages

---

**Note:** This is a proof-of-concept system designed for demonstration purposes. For production use, additional security, error handling, and optimization would be required.