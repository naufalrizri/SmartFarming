# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 10:17:33 2021

@author: Naufal Rizki
"""
import cv2
import numpy as np
import datetime
import urllib
import os
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("ngrok_test")  # Subscribe to the topic “digitest/test1”, receive any messages published on it


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
    imageStream(client, str(msg.payload))

def imageStream(client, url):
    now = time.time()
    
    while time.time() - now < 30:
        
        imgResp=urllib.request.urlopen(url[2:-1] + "/capture")
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    
        img=cv2.imdecode(imgNp,-1)
    
        # all the opencv processing is done here
        timenow = str(datetime.datetime.now())
        cv2.putText(img, timenow, (0, img.shape[1] - 90), font, .5,(255,255,255),2)
        cv2.imshow('test',img)
        image=img
        if ord('q')==cv2.waitKey(1):
            client.disconnect()
            break
        elif ord('s')==cv2.waitKey(1):
            timename = timenow[:10] + '_' + timenow[11:13] + "-" + timenow[14:16] + "-" + timenow[17:19]
            saved = cv2.imwrite(os.path.join(save_path, str(timename + '.jpg')), image)
            if saved:
                print("saved sucessfully!")

font = cv2.FONT_HERSHEY_SIMPLEX

save_path = r'E:\CCTV'

mqttc=mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message          
mqttc.connect("test.mosquitto.org", 1883, 60)                     # Mqtt broker
mqttc.loop_forever()
    
