import paho.mqtt.client as mqtt
import time
import yagmail

sez = []

def sendMail(temp):
    passw = "vdaxsnsqsglbivjq"
    user = 'zan.krajnc.kr@gmail.com'
    to = "zkrajnc@smart-com.si"
    subject = 'Temperatura v Lj'
    content = f"Trenutna temperatura v Ljubljani je {round(temp, 2)}°C"

    with yagmail.SMTP(user, passw) as yag:
        yag.send(to, subject, content)
        print('Sent email successfully')

def on_message(client, userdata, message):
    global sez
    msg = str(message.payload.decode("utf-8"))
    sez.append(float(msg))
    print("Received message: ", msg)


mqttBroker = "localhost"
port = 1883

client = mqtt.Client("Smartphone")
client.connect(mqttBroker, port) 

client.loop_start()

client.subscribe("TEMPERATURE")
client.on_message=on_message 

time.sleep(20)
client.loop_stop()

temp = sum(sez) / len(sez)
print(round(temp, 2))
sendMail(temp)