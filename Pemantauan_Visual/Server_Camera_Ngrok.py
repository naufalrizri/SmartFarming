# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:02:37 2021

@author: Naufal Rizki
"""

from pyngrok import ngrok
import paho.mqtt.client as mqtt
import time

import urllib
# import cv2
import numpy as np
import datetime
import os, sys
import urllib.request

mqttc=mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883, 60)                                   # Mqtt broker
ngrok.set_auth_token("1q9HgVeRZu268qk9Sg7CCGWKMxG_5gHw4mwKH2uxVNCTTexKN")       # Enter the registered Auth_Token
public_url = ngrok.connect("192.168.1.100:80")                                  # tunnel to host:port instead of localhost
print(public_url)                                                               # Displaying the ngrok_tunnel url

while True:
  time.sleep(1)
  print("publish")      
  mqttc.publish("ngrok_test",str(public_url)) #Publishing the created URL to "ngrok_test" Topic 
  mqttc.loop(2)
  time.sleep(30)
