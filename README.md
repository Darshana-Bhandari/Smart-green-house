🌱 Smart Greenhouse System (IoT)

📌 Overview
The Smart Greenhouse System is an IoT-based project designed to automate and optimize plant growth conditions. It uses sensors and a microcontroller to monitor environmental factors like temperature, humidity, and soil moisture, and automatically controls devices such as a fan and water pump.
This system reduces manual effort, improves efficiency, and ensures plants grow in optimal conditions through real-time monitoring and automation.

🚀 Features
🌡️ Temperature Monitoring using DHT22 sensor
💧 Soil Moisture Detection for automated irrigation
💨 Automatic Fan Control based on temperature
🚿 Water Pump Automation for plant watering
📟 LCD Display for real-time data visualization
🌐 IoT Integration (MQTT + Node-RED) for remote monitoring
⚠️ Alerts & Notifications for abnormal conditions

🛠️ Hardware Components
ESP32 Microcontroller
DHT22 Temperature & Humidity Sensor
Soil Moisture Sensor
Relay Module
Water Pump
Motor Fan
LCD Display (I2C)
Breadboard & Jumper Wires
Resistors
3.7V Battery
Potentiometer

💻 Software & Technologies
MicroPython (ESP32 programming)
Thonny IDE
MQTT Protocol
Node-RED Dashboard
Serial Monitor (Debugging)

⚙️ System Architecture
The system works as follows:
Sensors collect environmental data (temperature, humidity, soil moisture)
ESP32 processes the data
Based on threshold values:
Fan turns ON/OFF
Water pump activates/deactivates
Data is displayed on LCD
Data is sent to cloud (MQTT) for remote monitoring

🔄 Workflow
Read sensor data
Validate data
Compare with threshold values
Trigger actuators (fan/pump)
Display on LCD
Send data to dashboard
Repeat continuously

🧪 Testing & Results
Temperature and humidity monitoring
Soil moisture detection
Automatic fan control
Automatic irrigation system
LCD real-time display
MQTT data transmission

📊 Output Examples
Real-time temperature & humidity display
Soil moisture readings
Automatic fan activation at ≥ 24°C
Automatic pump activation when soil is dry
Live data on Node-RED dashboard

🔮 Future Improvements
📱 Mobile app integration
☀️ Solar power support
🌿 Additional sensors (CO₂, pH, Light)
📈 Data analytics & history tracking
🔐 Secure remote access (authentication)
🧠 Smart AI-based decision making

📚 Learning Outcomes
IoT system design and implementation
Sensor integration with ESP32
Automation using relay modules
Real-time data monitoring
MQTT and cloud communication
Debugging and testing embedded systems

👩‍💻 Author
Darshana Bhandari
This project is for educational purposes.
