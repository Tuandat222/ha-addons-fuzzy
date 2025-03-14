import paho.mqtt.client as mqtt
import skfuzzy as fuzz
import numpy as np
import json

# Hàm khi kết nối MQTT thành công
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("home/soil_data")  # Chủ đề nhận dữ liệu độ ẩm/nhiệt độ

# Hàm xử lý mỗi khi có dữ liệu mới
def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        moisture = float(data.get("moisture", 0))
        temperature = float(data.get("temperature", 0))

        # Rule logic đơn giản (thay thế fuzzy thật nếu chưa dùng scikit-fuzzy)
        if moisture < 30 and temperature > 30:
            result = "high"
        elif moisture < 60:
            result = "medium"
        else:
            result = "low"

        print(f"Moisture: {moisture} - Temp: {temperature} → Irrigation level: {result}")
        client.publish("home/irrigation_level", result)

    except Exception as e:
        print("Error processing message:", e)

# Kết nối MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.42", 1883, 60)  # 👉 Đổi IP thành MQTT broker của bạn

client.loop_forever()
