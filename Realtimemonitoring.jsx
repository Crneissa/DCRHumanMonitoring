import React from 'react';
import { Activity, Eye, Brain, Mic, Zap, Thermometer } from 'lucide-react';

const Dashboard = () => {
  return (
    <div className="min-h-screen bg-gray-900 text-white p-4 font-sans">
      {/* Header */}
      <div className="bg-gray-800 rounded-lg p-4 mb-4 flex items-center justify-between">
        <div className="flex items-center gap-4">
          <div className="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center">
            <Activity className="w-7 h-7" />
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
            <Activity className="w-5 h-5 text-blue-400" />
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
            <Eye className="w-5 h-5 text-blue-400" />
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
            <Brain className="w-5 h-5 text-blue-400" />
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
            <Mic className="w-5 h-5 text-blue-400" />
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
            <Zap className="w-5 h-5 text-yellow-400" />
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
            <Thermometer className="w-5 h-5 text-blue-400" />
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
};

export default Dashboard;
