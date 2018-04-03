#!/usr/bin/python

import os
import datetime
import traceback
import math
import random, string
import base64
import json
import paho.mqtt.client as mqtt
from time import sleep
from time import gmtime, strftime

packet_size=3000

def randomword(length):
 return ''.join(random.choice(string.lowercase) for i in range(length))


randomPayload = "{'test': '" + randomword(160) + "'}"

# MQTT
client = mqtt.Client()
client.username_pw_set("u","p")
client.connect("server.server.com", 17769, 60)
client.publish("JETSON", payload=randomPayload, qos=0, retain=True)
