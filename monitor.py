#!/usr/local/bin/python

import time
import requests
import sys
import Adafruit_DHT
import subprocess

# Sensor Details
sensor = Adafruit_DHT.DHT22
pin = '4'  # 'P8_11'
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')

cmd = "vcgencmd measure_temp| sed 's/[^0-9.]//g'"
piTemp = subprocess.check_output(cmd, shell=True)

sURL = 'http://192.168.1.17:5000/api/feeds'
oData = {'ip': '192.168.1.12',
         'v1': temperature, 'v2': humidity, 'v3': piTemp}
oCall = requests.post(sURL, data=oData)

print(oCall)
