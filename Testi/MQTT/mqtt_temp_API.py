import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import requests

def getTemp():
    podatki = {
        "appid": "524a3c97b3a1ac5e32d9e05b683ef523",
        "q": "Ljubljana",
        "units": "metric"}

    url = f"https://api.openweathermap.org/data/2.5/weather"

    klic = requests.get(url, params = podatki).json()
    temp = klic["main"]["temp"]

    return temp

mqttBroker = "localhost" 
port = 1883

client = mqtt.Client("Temperature_Lj")
client.connect(mqttBroker, port)

while True:
    temp = getTemp()
    #print(temp)
    client.publish("TEMPERATURE", temp)
    print("Just published " + str(temp) + " to topic TEMPERATURE")
    time.sleep(1)