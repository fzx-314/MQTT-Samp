import paho.mqtt.client as mqttClient
import time
import random
import math
import sys
import json

all_clients=[]
for i in range(1,11):
    all_clients.append('client'+str(i))
contact=[]

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

def location_generator():
    corr={'x':random.randrange(0,250,1),
          'y':random.randrange(0,250,1)}
    return corr

def distance(curr,to):
    return math.sqrt((to['x']-curr['x'])**2+(to['y']-curr['y'])**2)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    Dict = []
    msg = str (message.payload)
    Dict = eval(msg)
    topic1 = str (message.topic)
    if (distance ( curr, Dict ) < 20):
        clent_list = remove_prefix(topic1, 'location/')
        if (clent_list not in contact):
            contact.append(clent_list)

curr=location_generator()
#Task-1 Write code here
client_name = sys.argv[1]
broker_address = "127.0.0.1"
port = 1883
user = "admin"
password = "hivemq"

#Task-2 Write code here
 # create new instance MQTT client 
client = mqttClient.Client (client_name)

client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect(broker_address, port=port)  # connect to broker

client.loop_start()  # start the loop

#Task-3 Write code here
client.subscribe 
# loop to subsriber to all client, don't subscribe ourself
for i in range (10):
    if ( all_clients[i] != client_name ):
        client.subscribe("location/"+all_clients[i])

end_time=time.time()+15
while time.time() < end_time:
    # Task-4 Write code here
    client.publish("location/"+client_name,str(curr))
    time.sleep(0.5)
    curr=location_generator()
 
print("exiting")

print(contact)
time.sleep(10)
