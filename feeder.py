#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import requests
import sys
import subprocess

control = [5, 15]
servo = 17

# GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)


p = GPIO.PWM(servo, 50)  # 50hz frequency

p.start(0)
# Drop Food
time.sleep(0.3)
p.ChangeDutyCycle(15)
time.sleep(0.3)
# Reset to initial Location
p.ChangeDutyCycle(4)
time.sleep(0.3)
GPIO.cleanup()

sURL = 'http://192.168.1.17:5000/api/iot/started/00003'
oCall = requests.get(sURL)

print(oCall)
