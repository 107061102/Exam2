import paho.mqtt.client as paho
import time
import serial
import matplotlib.pyplot as plt
# https://os.mbed.com/teams/mqtt/wiki/Using-MQTT#python-client

# MQTT broker hosted on local machine
mqttc = paho.Client()

# Settings for connection
# TODO: revise host to your IP
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 9600)
host = "192.168.246.234"
topic = "Mbed"
# Callbacks
def on_connect(self, mosq, obj, rc):
    print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
    x0 = [1, 2, 3, 4, 5, 6, 7]
    x1 = [1, 2, 3, 4, 2, 3, 4]
    x2 = [1, 2, 3, 4, 5, 4, 3, 2]
    y0 = [3,3,3,3,3,3,3]
    y1 = [1,1,1,1,2,3,4]
    y2 = [3,2,1,2,3,4,5,4]

    info = msg.payload.decode().split(" ")
    if (info[2] == '0'):
        plt.scatter(x0, y0)
    elif (info[2] == '1'):
        plt.scatter(x1, y1)
    elif (info[2] == '2'):
        plt.scatter(x2, y2)

    if (info[1] == '10'):
        s.write(bytes("/FLIP/run 1\r", 'UTF-8'))
            
        
    


def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
    print("Unsubscribed OK")

# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

# Connect and subscribe
print("Connecting to " + host + "/" + topic)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic, 0)

# Publish messages from Python
num = 0
numcount = 0
while num != 5:
    ret = mqttc.publish(topic, "848 818 8.28\n", qos=0)
    if (ret[0] != 0):
            print("Publish failed")
    mqttc.loop()
    time.sleep(1.5)
    num += 1
# Loop forever, receiving messages
mqttc.loop_forever()

