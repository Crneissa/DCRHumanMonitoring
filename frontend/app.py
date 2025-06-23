import React, { useState } from 'react';

export default function SMRDashboard() {
  const [selectedComponent, setSelectedComponent] = useState(1);
  const [activeTab, setActiveTab] = useState('realtime');

  const components = [
    { id: 1, name: "Digital Control Room", status: "active" },
    { id: 2, name: "iPWR", status: "inactive" },
    { id: 3, name: "iPWR Interface", status: "inactive" },
    { id: 4, name: "SMR Operation Model", status: "inactive" },
    { id: 5, name: "HPSN", status: "inactive" },
    { id: 6, name: "Human Monitoring System", status: "inactive" },
    { id: 7, name: "Human Performance Management", status: "inactive" },
    { id: 8, name: "Human Simulator", status: "inactive" },
    { id: 9, name: "Control Room Simulator", status: "inactive" },
    { id: 10, name: "Human Controller", status: "inactive" },
    { id: 11, name: "Control Room Controller", status: "inactive" },
    { id: 12, name: "External Environment", status: "inactive" }
  ];

  const selectedComponentData = components.find(c => c.id === selectedComponent);

  const handleComponentClick = (componentId) => {
    setSelectedComponent(componentId);
    if (componentId === 6) {
      setActiveTab('realtime'); // Reset to first tab when selecting Human Monitoring System
    }
  };

  const renderHumanMonitoringContent = () => {
    if (activeTab === 'realtime') {
      return (
        <div className="w-full bg-gray-900 text-white p-4 font-sans">
          {/* Header */}
          <div className="bg-gray-800 rounded-lg p-4 mb-4 flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center">
                <div className="w-7 h-7 text-white">⚡</div>
              </div>
              <div>
                <h1 className="text-xl font-bold tracking-tight">Human Factors Monitor</h1>
                <p className="text-sm text-gray-400">Real-Time Performance Analytics</p>
              </div>
            </div>
            <div className="flex items-center gap-6 text-sm">
              <div className="text-center">
                <div className="text-3xl font-mono font-bold tracking-wider">28:45:23</div>
                <div className="text-gray-400 text-xs">Tuesday, June 11, 2025</div>
              </div>
              <div className="flex items-center gap-3">
                <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
                <div>
                  <span className="text-green-400 font-medium">Dr. Hassan Gaber</span>
                  <span className="text-gray-500 text-xs ml-2">ID: HG-2441</span>
                </div>
              </div>
              <button className="bg-green-600 px-4 py-2 rounded-lg flex items-center gap-2 font-medium">
                <div className="w-2 h-2 bg-white rounded-full"></div>
                Online
              </button>
            </div>
          </div>

          {/* Main Grid */}
          <div className="grid grid-cols-3 gap-4">
            {/* Health Monitoring Panel */}
            <div className="bg-gray-800 rounded-lg p-5 flex flex-col">
              <h2 className="text-lg font-semibold mb-5 flex items-center gap-2">
                <div className="w-5 h-5 text-blue-400">💓</div>
                Health Monitoring
              </h2>
              <div className="space-y-3.5 flex-1">
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Heart Rate</span>
                  <span className="text-lg font-medium">72 bpm</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Blood Pressure</span>
                  <span className="text-lg font-medium">120/80</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Body Temperature</span>
                  <span className="text-lg font-medium">36.5°C</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Respiratory Rate</span>
                  <span className="text-lg font-medium text-green-400">16 /min</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">HRV (RMSSD)</span>
                  <span className="text-lg font-medium">45ms</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Blood Oxygen</span>
                  <span className="text-lg font-medium">98%</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Hydration Level</span>
                  <span className="text-lg font-medium text-yellow-500">Moderate</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Sleep Quality</span>
                  <span className="text-lg font-medium">81%</span>
                </div>
              </div>
              <div className="mt-5 bg-red-900/30 border border-red-800/50 rounded-lg p-4">
                <div className="text-xs text-red-400 mb-2 font-medium uppercase tracking-wider">Fatigue Index</div>
                <div className="flex items-center gap-3">
                  <div className="text-3xl font-bold text-red-400">18%</div>
                  <div className="flex-1 bg-gray-700 rounded-full h-2.5">
                    <div className="bg-gradient-to-r from-red-600 to-red-400 h-2.5 rounded-full" style={{width: '18%'}}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* Eye Tracking & Visual Panel */}
            <div className="bg-gray-800 rounded-lg p-5 flex flex-col">
              <h2 className="text-lg font-semibold mb-5 flex items-center gap-2">
                <div className="w-5 h-5 text-blue-400">👁️</div>
                Eye Tracking & Visual
              </h2>
              <div className="space-y-3.5 flex-1">
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Gaze Direction</span>
                  <span className="text-lg font-medium">Center</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Pupil Size</span>
                  <span className="text-lg font-medium">4.2 mm</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Fixation Time</span>
                  <span className="text-lg font-medium">2.3 sec</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Saccade Rate</span>
                  <span className="text-lg font-medium">180/m</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Visual Acuity</span>
                  <span className="text-lg font-medium">20/20</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Screen Distance</span>
                  <span className="text-lg font-medium">65 cm</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-gray-400 text-sm">Eye Strain Level</span>
                  <span className="text-lg font-medium text-yellow-500">Low</span>
                </div>
                <div className="h-3.5"></div>
              </div>
              <div className="mt-5 bg-blue-900/30 border border-blue-800/50 rounded-lg p-4">
                <div className="text-xs text-blue-400 mb-2 font-medium uppercase tracking-wider">Attention Rate</div>
                <div className="flex items-center gap-3">
                  <div className="text-3xl font-bold text-blue-400">86%</div>
                  <div className="flex-1 bg-gray-700 rounded-full h-2.5">
                    <div className="bg-gradient-to-r from-blue-600 to-blue-400 h-2.5 rounded-full" style={{width: '86%'}}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* Facial Analysis Panel */}
            <div className="bg-gray-800 rounded-lg p-5 flex flex-col">
              <h2 className="text-lg font-semibold mb-5 flex items-center gap-2">
                <div className="w-5 h-5 text-blue-400">🧠</div>
                Facial Analysis
              </h2>
              <div className="flex-1">
                <div className="space-y-3.5 mb-5">
                  <div className="flex justify-between items-center">
                    <span className="text-gray-400 text-sm">Primary Emotion</span>
                    <span className="bg-gray-700 px-3 py-1 rounded-md text-sm font-medium">Neutral</span>
                  </div>
                  <div className="flex justify-between items-center">
                    <span className="text-gray-400 text-sm">Eye Symmetry</span>
                    <span className="text-green-400 font-medium">Normal</span>
                  </div>
                </div>
                <div className="space-y-2">
                  <div className="text-xs text-gray-400 font-medium uppercase tracking-wider mb-3">Emotion Distribution</div>
                  {[
                    { emotion: 'Neutral', value: 73, color: 'bg-gray-500' },
                    { emotion: 'Happy', value: 12, color: 'bg-green-500' },
                    { emotion: 'Focused', value: 8, color: 'bg-blue-500' },
                    { emotion: 'Tired', value: 4, color: 'bg-yellow-500' },
                    { emotion: 'Stressed', value: 2, color: 'bg-red-500' },
                    { emotion: 'Surprised', value: 1, color: 'bg-purple-500' },
                    { emotion: 'Angry', value: 0, color: 'bg-orange-500' },
                  ].map((item) => (
                    <div key={item.emotion} className="flex items-center gap-2">
                      <div className={`w-2 h-2 rounded-full ${item.color}`}></div>
                      <span className="text-xs w-16 text-gray-300">{item.emotion}</span>
                      <div className="flex-1 bg-gray-700 rounded-full h-1.5">
                        <div className={`${item.color} h-1.5 rounded-full transition-all duration-500`} style={{width: `${item.value}%`}}></div>
                      </div>
                      <span className="text-xs font-mono text-gray-400 w-8 text-right">{item.value}%</span>
                    </div>
                  ))}
                </div>
              </div>
              <div className="mt-5 bg-purple-900/30 border border-purple-800/50 rounded-lg p-4">
                <div className="text-xs text-purple-400 mb-2 font-medium uppercase tracking-wider">Stress Level</div>
                <div className="flex items-center gap-3">
                  <div className="text-3xl font-bold text-purple-400">23%</div>
                  <div className="flex-1 bg-gray-700 rounded-full h-2.5">
                    <div className="bg-gradient-to-r from-purple-600 to-purple-400 h-2.5 rounded-full" style={{width: '23%'}}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* Voice Analysis Panel */}
            <div className="bg-gray-800 rounded-lg p-5">
              <h2 className="text-lg font-semibold mb-5 flex items-center gap-2">
                <div className="w-5 h-5 text-blue-400">🎤</div>
                Voice Analysis
              </h2>
              <div className="grid grid-cols-2 gap-4 mb-4">
                <div className="text-center p-3 bg-gray-900/50 rounded-lg">
                  <div className="text-3xl font-bold">61.2K</div>
                  <div className="text-gray-400 text-xs font-medium uppercase tracking-wider">PROFILED</div>
                </div>
                <div className="text-center p-3 bg-gray-900/50 rounded-lg">
                  <div className="text-3xl font-bold">156 dB</div>
                  <div className="text-gray-400 text-xs font-medium uppercase tracking-wider">VOLUME</div>
                </div>
              </div>
              <div className="grid grid-cols-2 gap-4 mb-4">
                <div className="text-center p-3 bg-gray-900/50 rounded-lg">
                  <div className="text-2xl font-bold">108 WC</div>
                  <div className="text-gray-400 text-xs font-medium uppercase tracking-wider">SPEED</div>
                </div>
                <div className="text-center p-3 bg-gray-900/50 rounded-lg">
                  <div className="text-2xl font-bold">24</div>
                  <div className="text-gray-400 text-xs font-medium uppercase tracking-wider">TONE VARIATIONS</div>
                </div>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div className="text-center p-3 bg-gray-900/50 rounded-lg">
                  <div className="text-xl font-bold text-green-400">16%</div>
                  <div className="text-gray-400 text-xs font-medium uppercase tracking-wider">STRESS INDICATORS</div>
                </div>
                <div className="text-center p-3 bg-gray-900/50 rounded-lg">
                  <div className="text-xl font-bold">92.3s</div>
                  <div className="text-gray-400 text-xs font-medium uppercase tracking-wider">VOCAL COHERENCE</div>
                </div>
              </div>
            </div>

            {/* EEG Analysis Panel */}
            <div className="bg-gray-800 rounded-lg p-5 flex flex-col">
              <h2 className="text-lg font-semibold mb-5 flex items-center gap-2">
                <div className="w-5 h-5 text-yellow-400">⚡</div>
                EEG Analysis
              </h2>
              <div className="flex-1">
                <div className="grid grid-cols-2 gap-4 mb-4">
                  <div className="bg-gray-900/50 rounded-lg p-3">
                    <div className="text-gray-400 text-xs font-medium uppercase tracking-wider mb-1">Alpha</div>
                    <div className="flex items-baseline gap-2">
                      <span className="text-2xl font-bold">8.2</span>
                      <span className="text-gray-400 text-sm">High</span>
                    </div>
                  </div>
                  <div className="bg-gray-900/50 rounded-lg p-3">
                    <div className="text-gray-400 text-xs font-medium uppercase tracking-wider mb-1">Beta</div>
                    <div className="flex items-baseline gap-2">
                      <span className="text-2xl font-bold">12.7</span>
                      <span className="text-gray-400 text-sm">Normal</span>
                    </div>
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div className="bg-gray-900/50 rounded-lg p-3">
                    <div className="text-gray-400 text-xs font-medium uppercase tracking-wider mb-1">Theta</div>
                    <div className="flex items-baseline gap-2">
                      <span className="text-2xl font-bold">4.3</span>
                      <span className="text-gray-400 text-sm">Low</span>
                    </div>
                  </div>
                  <div className="bg-gray-900/50 rounded-lg p-3">
                    <div className="text-gray-400 text-xs font-medium uppercase tracking-wider mb-1">Delta</div>
                    <div className="flex items-baseline gap-2">
                      <span className="text-2xl font-bold">2.1</span>
                      <span className="text-gray-400 text-sm">Very Low</span>
                    </div>
                  </div>
                </div>
              </div>
              <div className="mt-5 bg-yellow-700/80 hover:bg-yellow-700 transition-colors text-yellow-100 py-4 rounded-lg text-center">
                <div className="text-lg font-bold">Moderate</div>
                <div className="text-xs opacity-80">Overall Activity</div>
              </div>
            </div>

            {/* Environmental Panel */}
            <div className="bg-gray-800 rounded-lg p-5 flex flex-col">
              <h2 className="text-lg font-semibold mb-5 flex items-center gap-2">
                <div className="w-5 h-5 text-blue-400">🌡️</div>
                Environmental
              </h2>
              <div className="flex-1">
                <div className="grid grid-cols-2 gap-x-6 gap-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-gray-400 text-sm">Temperature</span>
                    <span className="font-medium text-yellow-400">22°C</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-gray-400 text-sm">Humidity</span>
                    <span className="font-medium">45%</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-gray-400 text-sm">Air Quality</span>
                    <span className="font-medium text-green-400">Good</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-gray-400 text-sm">CO2 Level</span>
                    <span className="font-medium">470 ppm</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-gray-400 text-sm">Noise Level</span>
                    <span className="font-medium text-yellow-400">42 dB</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-gray-400 text-sm">Light Level</span>
                    <span className="font-medium text-yellow-400">Medium</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-gray-400 text-sm">UV Index</span>
                    <span className="font-medium text-green-400">Low</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-gray-400 text-sm">Barometric</span>
                    <span className="font-medium">1013 hPa</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-gray-400 text-sm">Air Flow</span>
                    <span className="font-medium text-green-400">Low</span>
                  </div>
                  <div className="flex items-center justify-between">
                    <span className="text-gray-400 text-sm">Vibration</span>
                    <span className="font-medium">0.01 m/s²</span>
                  </div>
                </div>
              </div>
              <div className="mt-5 bg-teal-900/30 border border-teal-800/50 rounded-lg p-4">
                <div className="text-center">
                  <div className="text-xs text-teal-400 mb-1 font-medium uppercase tracking-wider">Environmental Score</div>
                  <div className="text-3xl font-bold text-teal-400">8.3/10</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      );
    } else {
      return (
        <div className="w-full bg-gray-900 text-white">
          {/* Header */}
          <div className="bg-gray-800 border-b border-gray-700 p-4">
            <div className="flex items-center justify-between">
              <div>
                <h1 className="text-2xl font-bold text-blue-400">Human Factors Monitor</h1>
                <p className="text-gray-400 text-sm">Analytics Data</p>
              </div>
              <div className="flex items-center space-x-4">
                {/* Navigation */}
                <select className="bg-gray-700 text-white px-3 py-2 rounded border border-gray-600">
                  <option>Dr. Hossam Gabar</option>
                </select>
                <select className="bg-gray-700 text-white px-3 py-2 rounded border border-gray-600">
                  <option>Navigation</option>
                </select>
                <select className="bg-gray-700 text-white px-3 py-2 rounded border border-gray-600">
                  <option>Unit 5</option>
                </select>
                <div className="text-right">
                  <div className="text-sm text-gray-300 flex items-center">
                    🕐 28:45:23
                  </div>
                  <div className="text-xs text-gray-500">
                    June 23, 2025
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Tab Navigation */}
          <div className="bg-gray-800 border-b border-gray-700">
            <div className="flex space-x-1 p-4">
              <button className="flex items-center space-x-2 px-4 py-2 rounded bg-blue-600 text-white">
                <span>📊</span>
                <span>Overview</span>
              </button>
              <button className="flex items-center space-x-2 px-4 py-2 rounded text-gray-300 hover:text-white hover:bg-gray-700">
                <span>🧠</span>
                <span>Detailed Analytics</span>
              </button>
              <button className="flex items-center space-x-2 px-4 py-2 rounded text-gray-300 hover:text-white hover:bg-gray-700">
                <span>👤</span>
                <span>AI Predictions</span>
              </button>
            </div>
          </div>

          {/* Main Content */}
          <div className="p-6 space-y-6">
            {/* Top Metrics */}
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
              <div className="bg-gray-800 rounded-lg p-4 border border-gray-700">
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center space-x-2">
                    <span className="w-5 h-5 text-red-400">💗</span>
                    <span className="text-gray-300 text-sm">Heart Rate</span>
                  </div>
                </div>
                <div className="text-2xl font-bold text-white">
                  56 <span className="text-sm text-gray-400">BPM</span>
                </div>
              </div>
              <div className="bg-gray-800 rounded-lg p-4 border border-gray-700">
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center space-x-2">
                    <span className="w-5 h-5 text-blue-400">🧠</span>
                    <span className="text-gray-300 text-sm">Attention</span>
                  </div>
                </div>
                <div className="text-2xl font-bold text-white">
                  88 <span className="text-sm text-gray-400">%</span>
                </div>
              </div>
              <div className="bg-gray-800 rounded-lg p-4 border border-gray-700">
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center space-x-2">
                    <span className="w-5 h-5 text-yellow-400">⚠️</span>
                    <span className="text-gray-300 text-sm">Stress Level</span>
                  </div>
                </div>
                <div className="text-2xl font-bold text-white">
                  54 <span className="text-sm text-gray-400">%</span>
                </div>
              </div>
              <div className="bg-gray-800 rounded-lg p-4 border border-gray-700">
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center space-x-2">
                    <span className="w-5 h-5 text-purple-400">📊</span>
                    <span className="text-gray-300 text-sm">Fatigue Index</span>
                  </div>
                </div>
                <div className="text-2xl font-bold text-white">
                  29 <span className="text-sm text-gray-400">%</span>
                </div>
              </div>
            </div>

            {/* Comprehensive Voice Analysis */}
            <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
              <h3 className="text-lg font-semibold text-white mb-4 flex items-center">
                <span className="w-5 h-5 mr-2">🎤</span>
                Comprehensive Voice Analysis
              </h3>
              <div className="space-y-4">
                <div className="mb-4">
                  <div className="flex justify-between mb-1">
                    <span className="text-gray-300 text-sm">Voice Stress Level</span>
                    <span className="text-white text-sm">57%</span>
                  </div>
                  <div className="w-full bg-gray-700 rounded-full h-2">
                    <div className="h-2 rounded-full transition-all duration-300 bg-yellow-500" style={{width: '57%'}}></div>
                  </div>
                </div>
                <div className="mb-4">
                  <div className="flex justify-between mb-1">
                    <span className="text-gray-300 text-sm">Speech Clarity</span>
                    <span className="text-white text-sm">97%</span>
                  </div>
                  <div className="w-full bg-gray-700 rounded-full h-2">
                    <div className="h-2 rounded-full transition-all duration-300 bg-green-500" style={{width: '97%'}}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* Facial Analysis */}
            <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-lg font-semibold text-white flex items-center">
                  <span className="w-5 h-5 mr-2">👤</span>
                  Facial Analysis
                </h3>
                <span className="text-sm bg-purple-900 text-purple-300 px-2 py-1 rounded">DISGUST</span>
              </div>
              <div className="space-y-3">
                <div className="mb-4">
                  <div className="flex justify-between mb-1">
                    <span className="text-gray-300 text-sm">Confidence</span>
                    <span className="text-white text-sm">95%</span>
                  </div>
                  <div className="w-full bg-gray-700 rounded-full h-2">
                    <div className="h-2 rounded-full transition-all duration-300 bg-blue-500" style={{width: '95%'}}></div>
                  </div>
                </div>
                <div className="mb-4">
                  <div className="flex justify-between mb-1">
                    <span className="text-gray-300 text-sm">Stress Level</span>
                    <span className="text-white text-sm">54%</span>
                  </div>
                  <div className="w-full bg-gray-700 rounded-full h-2">
                    <div className="h-2 rounded-full transition-all duration-300 bg-yellow-500" style={{width: '54%'}}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* Eye Tracking */}
            <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-lg font-semibold text-white flex items-center">
                  <span className="w-5 h-5 mr-2">👁️</span>
                  Eye Tracking
                </h3>
                <span className="text-sm bg-green-900 text-green-300 px-2 py-1 rounded">RIGHT</span>
              </div>
              <div className="space-y-3">
                <div className="flex justify-between text-sm">
                  <span className="text-gray-300">Blink Rate</span>
                  <span className="text-white">22.6 /min</span>
                </div>
                <div className="mb-4">
                  <div className="flex justify-between mb-1">
                    <span className="text-gray-300 text-sm">Attention Level</span>
                    <span className="text-white text-sm">88%</span>
                  </div>
                  <div className="w-full bg-gray-700 rounded-full h-2">
                    <div className="h-2 rounded-full transition-all duration-300 bg-green-500" style={{width: '88%'}}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* Health Metrics */}
            <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
              <h3 className="text-lg font-semibold text-white flex items-center mb-4">
                <span className="w-5 h-5 mr-2">💗</span>
                Health Metrics
              </h3>
              <div className="space-y-3">
                <div className="flex justify-between text-sm">
                  <span className="text-gray-300">Blood Pressure</span>
                  <span className="text-white">130/80 mmHg</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="text-gray-300">HRV</span>
                  <span className="text-white">85.3 ms</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="text-gray-300">Temperature</span>
                  <span className="text-white">98.6°F</span>
                </div>
                <div className="mb-4">
                  <div className="flex justify-between mb-1">
                    <span className="text-gray-300 text-sm">Fatigue Index</span>
                    <span className="text-white text-sm">29%</span>
                  </div>
                  <div className="w-full bg-gray-700 rounded-full h-2">
                    <div className="h-2 rounded-full transition-all duration-300 bg-purple-500" style={{width: '29%'}}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* 12-Hour Complete Performance Overview */}
            <div className="bg-gray-800 rounded-lg p-6 border border-gray-700">
              <h3 className="text-lg font-semibold text-white mb-4">12-Hour Complete Performance Overview</h3>
              <div className="bg-gray-700 rounded p-4">
                <svg width="100%" height="300" viewBox="0 0 800 300">
                  {/* Grid lines */}
                  <defs>
                    <pattern id="grid" width="40" height="30" patternUnits="userSpaceOnUse">
                      <path d="M 40 0 L 0 0 0 30" fill="none" stroke="#374151" strokeWidth="1" strokeDasharray="2,2"/>
                    </pattern>
                  </defs>
                  <rect width="100%" height="100%" fill="url(#grid)" />
                  
                  {/* Lines */}
                  <polyline fill="none" stroke="#ef4444" strokeWidth="2" 
                    points="50,180 120,170 190,190 260,150 330,140 400,120 470,90 540,100 610,120 680,80 750,90 780,100"/>
                  <polyline fill="none" stroke="#8b5cf6" strokeWidth="2" 
                    points="50,160 120,170 190,180 260,200 330,210 400,180 470,130 540,120 610,110 680,90 750,80 780,90"/>
                  <polyline fill="none" stroke="#10b981" strokeWidth="2" 
                    points="50,200 120,120 190,90 260,60 330,50 400,90 470,130 540,150 610,170 680,180 750,120 780,120"/>
                  <polyline fill="none" stroke="#f59e0b" strokeWidth="2" 
                    points="50,210 120,200 190,210 260,220 330,215 400,180 470,160 540,150 610,140 680,130 750,160 780,170"/>
                  <polyline fill="none" stroke="#06b6d4" strokeWidth="2" 
                    points="50,150 120,130 190,110 260,100 330,95 400,120 470,140 540,150 610,160 680,170 750,140 780,130"/>
                  
                  {/* Legend */}
                  <text x="50" y="290" fill="#ef4444" fontSize="12">Stress Level</text>
                  <text x="150" y="290" fill="#8b5cf6" fontSize="12">Fatigue Index</text>
                  <text x="250" y="290" fill="#10b981" fontSize="12">Attention Level</text>
                  <text x="370" y="290" fill="#f59e0b" fontSize="12">Voice Stress</text>
                  <text x="470" y="290" fill="#06b6d4" fontSize="12">EEG Alpha</text>
                </svg>
              </div>
            </div>
          </div>
        </div>
      );
    }
  };

  const renderDefaultContent = () => (
    <div className="text-center">
      <div className="text-8xl font-bold text-blue-500 mb-6 opacity-80">{selectedComponent}</div>
      <h3 className="text-3xl font-semibold text-white mb-3">{selectedComponentData?.name}</h3>
      <p className="text-gray-500 text-lg">Content area for this component</p>
      <div className="mt-8 pt-8 border-t border-gray-800">
        <p className="text-sm text-gray-600">System ready for implementation</p>
      </div>
    </div>
  );

  return (
    <div className="h-screen bg-black overflow-hidden">
      {/* Header */}
      <div className="bg-gray-900 border-b-2 border-gray-800 px-6 py-3">
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-xl font-semibold text-white">SMR Digital Control Room Dashboard</h1>
            <p className="text-xs text-gray-500 mt-1">Ontario Tech University - Smart Energy Systems Lab</p>
          </div>
          <div className="text-right">
            <p className="text-sm text-gray-300">Operator: OP-001</p>
            <p className="text-xs text-gray-500">Dr. Hossam Gaber</p>
          </div>
          <div className="text-right">
            <p className="text-2xl font-mono text-white font-semibold">20:44:36</p>
            <p className="text-xs text-gray-500">Jun 17, 2025</p>
          </div>
        </div>
      </div>

      {/* Main Layout */}
      <div className="flex h-full bg-gray-950">
        {/* Sidebar */}
        <div className="w-64 bg-gray-900 border-r-2 border-gray-800 h-full overflow-y-auto">
          <div className="p-4">
            <h2 className="text-white font-semibold mb-4 text-sm uppercase tracking-wider">System Components</h2>
            <div className="space-y-1">
              {components.map((component) => (
                <button
                  key={component.id}
                  onClick={() => handleComponentClick(component.id)}
                  className={`w-full px-4 py-3 rounded text-left transition-all duration-200 ${
                    selectedComponent === component.id
                      ? 'bg-blue-700 text-white shadow-lg transform scale-105'
                      : 'bg-gray-800 text-gray-400 hover:bg-gray-700 hover:text-gray-300'
                  }`}
                >
                  <div className="flex items-center">
                    <span className="mr-3 text-xs font-mono bg-gray-700 px-2 py-1 rounded">{component.id}</span>
                    <span className="text-sm">{component.name}</span>
                  </div>
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Main Content Area */}
        <div className="flex-1 bg-gray-950 p-4 overflow-hidden">
          <div className="bg-gray-900 rounded-lg border-2 border-gray-800 flex flex-col" style={{height: 'calc(100vh - 100px)'}}>
            {/* Component Header */}
            <div className="border-b-2 border-gray-800 px-6 py-4">
              <div className="flex items-center justify-between">
                <h2 className="text-lg font-semibold text-white">
                  Component {selectedComponent}: {selectedComponentData?.name}
                </h2>
                <div className="flex items-center space-x-2">
                  <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
                  <span className="text-green-500 text-sm font-medium uppercase">Active</span>
                </div>
              </div>
            </div>

            {/* Tabs for Human Monitoring System */}
            {selectedComponent === 6 && (
              <div className="border-b border-gray-800 px-6">
                <div className="flex space-x-1">
                  <button
                    onClick={() => setActiveTab('realtime')}
                    className={`px-4 py-3 text-sm font-medium transition-all duration-200 border-b-2 ${
                      activeTab === 'realtime'
                        ? 'text-blue-400 border-blue-400'
                        : 'text-gray-400 border-transparent hover:text-gray-300'
                    }`}
                  >
                    Real Time Monitoring
                  </button>
                  <button
                    onClick={() => setActiveTab('analytics')}
                    className={`px-4 py-3 text-sm font-medium transition-all duration-200 border-b-2 ${
                      activeTab === 'analytics'
                        ? 'text-blue-400 border-blue-400'
                        : 'text-gray-400 border-transparent hover:text-gray-300'
                    }`}
                  >
                    Analytics Report & Prediction
                  </button>
                </div>
              </div>
            )}

            {/* Component Display Area */}
            <div className="flex-1 p-4 overflow-y-auto">
              <div className="bg-gray-950 rounded-lg border-2 border-gray-800 min-h-full flex items-start justify-center">
                {selectedComponent === 6 ? renderHumanMonitoringContent() : renderDefaultContent()}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

