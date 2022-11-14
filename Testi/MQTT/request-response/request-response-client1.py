#!C:/python36/python.exe
#!/usr/bin/env python3
##demo code provided by Steve Cope at www.steves-internet-guide.com
##email steve@steves-internet-guide.com
##Free to use for any purpose
##If you like and use this code you can
##buy me a drink here https://www.paypal.me/StepenCope

import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes 
import time,logging,sys

client_id="testclient2"
mqttv=mqtt.MQTTv5
messages=[]
host = 'localhost'
port=1883
pub_topic="test"

def on_publish(client, userdata, mid):
    print("published")

def on_connect(client, userdata, flags, reasonCode,properties=None):
    print('Connected ',flags)
    print('Connected properties',properties)
    print('Connected ',reasonCode)



def on_message(client, userdata, message):

    msg=str(message.payload.decode("utf-8"))
    messages.append(msg)
    print("properties",message.properties)
    count=int.from_bytes(message.properties.CorrelationData,"big")
    print("correlation count=",count)
    print('RECV Topic = ',message.topic)
    print('RECV MSG =', msg)
    client.message_received_flag=True


def on_disconnect(client, userdata, rc,properties):
    print('Received Disconnect ',rc)

def on_subscribe(client, userdata, mid, granted_qos,properties=None):
    print('SUBSCRIBED')

def on_unsubscribe(client, userdata, mid, properties, reasonCodes):
    print('UNSUBSCRIBED') 
    



print("creating client")

client = mqtt.Client("client1",protocol=mqttv)


client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_publish = on_publish

properties=None
client.connect(host,port,properties=properties)
client.loop_start()

client.subscribe('org/responses/client1')
time.sleep(2)
client.message_received_flag=False
print("Publish response topic")
msg_out1="test message from client 1"
properties=Properties(PacketTypes.PUBLISH)
properties.ResponseTopic='org/responses/client1'
print("starting client 1")
count=1
while True:
    properties.CorrelationData=bytes([count])
    print("send count=",count)
    client.publish('org/common',"test from client1",properties=properties)

    while not client.message_received_flag:
        time.sleep(1) #wait for message
    client.message_received_flag=False
    if len(messages)==0:
        print("test failed")
    else:
        msg=messages.pop()
        if msg==msg_out1:
            print("test succeeded")
    time.sleep(5)
    count+=1

client.disconnect()



