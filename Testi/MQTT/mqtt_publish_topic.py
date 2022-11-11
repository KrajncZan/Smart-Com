import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

mqttBroker = "localhost" 
port = 1883

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker, port)

while True:
    randNumber = round(uniform(19, 21), 2)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)