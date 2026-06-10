# Smart Greenhouse IoT System

## Overview
The Smart Greenhouse System is an IoT-based automation project designed using ESP32. It monitors environmental conditions such as temperature, humidity, and soil moisture, and automatically controls devices like a fan and water pump to maintain optimal plant growth conditions.

The system also supports MQTT-based communication and a Node-RED dashboard for real-time monitoring and control.

---

## Features
- Real-time temperature and humidity monitoring using DHT22
- Soil moisture-based automated irrigation system
- Automatic fan control based on temperature threshold
- Water pump automation for irrigation
- LCD display for real-time sensor data
- MQTT-based cloud communication
- Node-RED dashboard for remote monitoring
- Alert system for abnormal conditions

---

## Hardware Components
- ESP32 Microcontroller
- DHT22 Temperature and Humidity Sensor
- Soil Moisture Sensor
- Relay Module
- Water Pump
- Fan
- LCD Display (I2C)
- Breadboard and jumper wires
- Power supply

---

## Software and Technologies
- MicroPython for ESP32
- Thonny IDE
- MQTT Protocol
- Node-RED Dashboard
- Serial Monitor for debugging

---

## System Architecture
1. Sensors collect environmental data
2. ESP32 processes sensor readings
3. Threshold-based control logic is applied
   - Fan activates based on temperature
   - Pump activates based on soil moisture level
4. Data is displayed on LCD
5. Data is sent to MQTT broker
6. Node-RED visualizes real-time data

---

## Workflow
Sensor reading → Data processing → Threshold comparison → Actuator control → LCD display → MQTT transmission → Continuous loop

---

## Outputs
- Real-time environmental monitoring
- Automatic irrigation system
- Smart fan control
- Live dashboard on Node-RED
- Continuous sensor data updates

---

## Future Improvements
- Mobile application integration
- Solar power support
- Additional sensors such as CO2, pH, and light
- Data analytics and historical tracking
- Secure authentication for remote access
- AI-based decision making for smart farming

---

## Author
Darshana Bhandari

This project is developed for educational purposes in IoT and embedded systems.
