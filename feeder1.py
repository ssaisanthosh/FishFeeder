#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

#control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
control = [5,15]

servo = 17

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(servo,GPIO.OUT)
# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

p=GPIO.PWM(servo,50)# 50hz frequency

p.start(0)# starting duty cycle ( it set the servo to 0 degree )

#try:
#       while True:
#           for x in range(11):
time.sleep(0.3);
p.ChangeDutyCycle(15);
time.sleep(0.3);
#             p.stop();
#p.start(7.5);
p.ChangeDutyCycle(4);
time.sleep(0.3);
#	     p.stop();	
#	     GPIO.cleanup();
#	     duty = float(5) / 10.0 + 2.5
#	     p.ChangeDutyCycle(5);
#	     print duty;
#	     time.sleep(1);
#	     p.stop();
#             print x
#           
#           for x in range(9,0,-1):
#           for x in range(2):
#             p.ChangeDutyCycle(control[x])
#             time.sleep(0.03)
#             print x
#             p.stop()
#             p.ChangeDutyCycle(control[0])
#             time.sleep(0.05)
#             print x

#             p.ChangeDutyCycle(control[1])
#             time.sleep(0.05)
#             print x

#             p.ChangeDutyCycle(control[0])
#             time.sleep(0.05)
#             print x

#             p.ChangeDutyCycle(control[1])
#             time.sleep(0.1)

#	     p.stop()
           
#except KeyboardInterrupt:
GPIO.cleanup()
