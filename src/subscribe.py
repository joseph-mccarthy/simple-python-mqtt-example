import paho.mqtt.client as paho # import the mqtt library (pip3 install paho-mqtt)

broker = "broker" # broker address
topic = "examples/#" # topic name to subscribe to in this case we are interested in everything under examples. This
                     # this will include the random_number topic that publish.py is calling to.

def on_connect_callback(client,userdata,flags,rc): # define the on_connect callback method    
    client.subscribe(topic) # subscribe to to the topic, best to do in on_connect so if connection is lost topic is added again

client = paho.Client(client_id="subscriber-001-example", # subscriber id
                        transport="tcp",  # the connection protocol
                        reconnect_on_failure= True # attempt to reconnect on failure 
                        )

client.on_connect=on_connect_callback # assign callback method to on_connect handle
client.connect(broker) # connect to the broker

def on_message(client,userdata,message):    
    message_data = str(message.payload.decode('utf-8')) # decode the message that was recieved
    print(f"{message.topic} - {message_data}") # print the message payload to console

client.on_message = on_message # assign the on_message_callback method to the on_message handle
client.loop_forever()  # start networking daemon