import time # import time so we can sleep the infinite loop between iterations
import paho.mqtt.client as paho # import the mqtt library (pip3 install paho-mqtt)
import random # import to generage random numbers

def on_connect_callback(client,userdata,flags,rc): # define the on_connect callback method
    print("connection callback...")

def on_publish_callback(client, userdata, mid): # define the on_publish callback method
    print("published data...")


broker = "broker.hivemq.com" # free mqtt broker
topic = "jbm-example" # example topic name

client = paho.Client(client_id="publisher-001-jbm-example", # id of this client sending data
                        transport="tcp", ## protocol
                        reconnect_on_failure= True ## attempt to reconnect on failure
                        )

client.on_connect=on_connect_callback # assign callback method to on_connect handle
client.on_publish=on_publish_callback # assign callback method to the on_publish handle

client.connect(broker) # connect to the broker

while True: # infinite loop to keep publishing a random number
    random_number = random.randint(1,100) # generate a random number between 1 and 100
    client.publish(topic,random_number) # publish this number to the topic
    time.sleep(10) # sleep for 10 seconds