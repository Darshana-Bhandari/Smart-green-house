#main.py
import dht
import network
import ujson
import time
from machine import Pin, ADC
from umqtt.simple import MQTTClient
print("Smart Green House System Started 🌱")

# -------- DHT SENSOR --------
dht_sensor = dht.DHT22(Pin(4))

# -------- WIFI --------
Wifi_ssid = "IIC_WIFI"
Wifi_pass = "!tah@rIntl2025"

# -------- MQTT --------
MQTT_CLIENT_ID = "290389975a754872a92f77eb36aed48e"
MQTT_BROKER = "290389975a754872a92f77eb36aed48e.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_SSL = True
MQTT_USER = "shradhalimbu"
MQTT_PASS = "Shradha@123"
MQTT_SQT_PARAMS = {"server_hostname": MQTT_BROKER}

MQTT_TOPIC1 = "IOT/DHT"
MQTT_TOPIC2 = "IOT/MOTOR"
MQTT_TOPIC3 = "IOT/PUMP"

# -------- LCD --------
from machine import SoftI2C
from machine_i2c_lcd import I2cLcd

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = SoftI2C(sda=Pin(21), scl=Pin(22), freq=100000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# -------- SENSORS & ACTUATORS --------
SOIL_PIN = 34
PUMP_PIN = 27
FAN_PIN = 26

soil_sensor = ADC(Pin(SOIL_PIN))
soil_sensor.atten(ADC.ATTN_11DB)

pump = Pin(PUMP_PIN, Pin.OUT)
fan = Pin(FAN_PIN, Pin.OUT)

# -------- WIFI CONNECT --------
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(Wifi_ssid, Wifi_pass)
    while not wlan.isconnected():
        time.sleep(0.5)
    print("WiFi connected")

# -------- MQTT CONNECT --------
def connect_mqtt():
    client = MQTTClient(
        MQTT_CLIENT_ID,
        MQTT_BROKER,
        port=MQTT_PORT,
        ssl=MQTT_SSL,
        user=MQTT_USER,
        password=MQTT_PASS,
        ssl_params=MQTT_SQT_PARAMS
    )
    client.connect()
    return client

def set_cb(topic, msg):
    print(topic.decode(), msg.decode())

# -------- SETUP --------
connect_wifi()
client = connect_mqtt()
client.set_callback(set_cb)
client.subscribe(MQTT_TOPIC1)
client.subscribe(MQTT_TOPIC2)
client.subscribe(MQTT_TOPIC3)

# -------- LOOP --------
while True:
    try:
        # Read DHT
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()

        # Read soil moisture
        soil_value = soil_sensor.read()
        print("Soil Moisture Value:", soil_value)

        # -------- FAN LOGIC --------
        if temp <  24:
            fan.value(1)          # Fan ON
            fan_state = "OFF"
        else:
            fan.value(0)          # Fan OFF
            fan_state = "ON"

        print("Fan Relay:", fan_state)

        # -------- PUMP LOGIC --------
        if soil_value < 2400:     # Dry soil
            pump.value(0)         # Pump ON
            pump_state = "ON"
            client.publish(MQTT_TOPIC3, "ON")
        else:
            pump.value(1)         # Pump OFF
            pump_state = "OFF"
            client.publish(MQTT_TOPIC3, "OFF")

        print("Pump Relay:", pump_state)

        # -------- LCD DISPLAY --------
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("T:{:.1f}C F:{}".format(temp, fan_state))

        lcd.move_to(0, 1)
        lcd.putstr("H:{}% P:{}".format(int(hum), pump_state))

        # -------- MQTT DATA --------
        client.publish(
            MQTT_TOPIC1,
            ujson.dumps({
                "temperature": temp,
                "humidity": hum,
                "soil": soil_value
            })
        )

        client.check_msg()

    except Exception as e:
        print("Error:", e)

    time.sleep(5)