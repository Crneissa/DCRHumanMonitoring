const express = require("express");
const http = require("http");
const socketIo = require("socket.io");
const { MongoClient } = require("mongodb");
const cors = require("cors");
const path = require("path");

class SensorDataServer {
  constructor() {
    this.app = express();
    this.server = http.createServer(this.app);
    this.io = socketIo(this.server, {
      cors: {
        origin: "*",
        methods: ["GET", "POST"],
      },
    });

    this.mongoClient = null;
    this.db = null;
    this.collection = null;
    this.isConnected = false;
    this.pollInterval = null;
    this.lastSeenTimestamps = null;

    // Store latest data for each sensor
    this.latestData = {
      emotion: null,
      gaze: null,
      stress: null,
    };

    this.setupMiddleware();
    this.setupRoutes();
    this.setupSocketHandlers();
  }

  setupMiddleware() {
    // Enable CORS for all routes
    this.app.use(cors());

    // Parse JSON bodies
    this.app.use(express.json());

    // Serve static files from current directory
    this.app.use(express.static("."));
  }

  setupRoutes() {
    // Health check endpoint
    this.app.get("/health", (req, res) => {
      res.json({
        status: "ok",
        database: this.isConnected ? "connected" : "disconnected",
        timestamp: new Date().toISOString(),
      });
    });

    // Get latest sensor data
    this.app.get("/api/latest", (req, res) => {
      res.json(this.latestData);
    });

    // Get sensor data history
    this.app.get("/api/history/:sensorType", async (req, res) => {
      try {
        const { sensorType } = req.params;
        const limit = parseInt(req.query.limit) || 50;

        if (!this.isConnected) {
          return res.status(500).json({ error: "Database not connected" });
        }

        const data = await this.collection
          .find({ sensor_type: sensorType })
          .sort({ timestamp: -1 })
          .limit(limit)
          .toArray();

        res.json(data.reverse()); // Return in chronological order
      } catch (error) {
        console.error("Error fetching history:", error);
        res.status(500).json({ error: "Failed to fetch data" });
      }
    });

    // Serve the frontend
    this.app.get("/", (req, res) => {
      res.sendFile(path.join(__dirname, "index.html"));
    });
  }

  setupSocketHandlers() {
    this.io.on("connection", (socket) => {
      console.log("Client connected:", socket.id);

      // Send latest data to newly connected client
      socket.emit("latest-data", this.latestData);

      socket.on("disconnect", () => {
        console.log("Client disconnected:", socket.id);
      });
    });
  }

  async connectToMongoDB() {
    try {
      console.log("Connecting to MongoDB...");
      this.mongoClient = new MongoClient("mongodb://127.0.0.1:27017/");
      await this.mongoClient.connect();

      this.db = this.mongoClient.db("sensor_data");
      this.collection = this.db.collection("readings");
      this.isConnected = true;

      console.log("Connected to MongoDB successfully");

      // Clear all previous readings for fresh start
      await this.clearPreviousReadings();

      // Start watching for changes
      this.watchDatabaseChanges();
    } catch (error) {
      console.error("Failed to connect to MongoDB:", error);
      this.isConnected = false;
    }
  }

  async clearPreviousReadings() {
    try {
      const result = await this.collection.deleteMany({});
      console.log(
        `Cleared ${result.deletedCount} previous readings for fresh start`
      );
    } catch (error) {
      console.error("Error clearing previous readings:", error);
    }
  }

  watchDatabaseChanges() {
    // For POC: Use polling instead of Change Streams (which require replica sets)
    // Store last seen timestamps for each sensor type
    this.lastSeenTimestamps = {
      emotion: null,
      gaze: null,
      stress: null,
    };

    // Poll for new data every 500ms
    this.pollInterval = setInterval(async () => {
      try {
        for (const sensorType of ["emotion", "gaze", "stress"]) {
          const query = { sensor_type: sensorType };

          // If we have a last seen timestamp, only get newer data
          if (this.lastSeenTimestamps[sensorType]) {
            query.timestamp = { $gt: this.lastSeenTimestamps[sensorType] };
          }

          const newData = await this.collection
            .find(query)
            .sort({ timestamp: -1 })
            .limit(1)
            .toArray();

          if (newData.length > 0) {
            const latestReading = newData[0];

            // Update last seen timestamp
            this.lastSeenTimestamps[sensorType] = latestReading.timestamp;

            // Update latest data for the sensor type
            this.latestData[sensorType] = {
              value: latestReading.value,
              timestamp: latestReading.timestamp,
              operator_name: latestReading.operator_name,
            };

            console.log("New sensor data:", latestReading);

            // Broadcast to all connected clients
            this.io.emit("sensor-update", {
              sensor_type: sensorType,
              data: this.latestData[sensorType],
            });
          }
        }
      } catch (error) {
        console.error("Error polling for new data:", error);
      }
    }, 500);

    console.log("Started polling for database changes (every 500ms)");
  }

  async start(port = 3000) {
    try {
      // Connect to MongoDB first
      await this.connectToMongoDB();

      // Start the server
      this.server.listen(port, () => {
        console.log(`\n=== Sensor Data Server ===`);
        console.log(`Server running on http://localhost:${port}`);
        console.log(
          `Database: ${this.isConnected ? "Connected" : "Disconnected"}`
        );
        console.log("=========================\n");
      });
    } catch (error) {
      console.error("Failed to start server:", error);
    }
  }

  async stop() {
    try {
      // Clear polling interval
      if (this.pollInterval) {
        clearInterval(this.pollInterval);
      }

      if (this.mongoClient) {
        await this.mongoClient.close();
      }
      this.server.close();
      console.log("Server stopped");
    } catch (error) {
      console.error("Error stopping server:", error);
    }
  }
}

// Handle graceful shutdown
process.on("SIGINT", async () => {
  console.log("\nShutting down server...");
  if (global.server) {
    await global.server.stop();
  }
  process.exit(0);
});

// Start the server
const server = new SensorDataServer();
global.server = server;
server.start(3000);
