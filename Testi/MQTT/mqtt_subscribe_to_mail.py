import paho.mqtt.client as mqtt
import time
import yagmail

def sendMail(temp):
    passw = "r****"
    user = 'zan.krajnc.kr@gmail.com'
    to = "zan.krajnc.kr@gmail.com"
    subject = 'Temperatura'
    content = f"Trenutno je temperatura {temp}"

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "localhost"
port = 1883

client = mqtt.Client("Smartphone")
client.connect(mqttBroker, port) 

client.loop_start()

client.subscribe("TEMPERATURE")
client.on_message=on_message 

time.sleep(30)
client.loop_stop()