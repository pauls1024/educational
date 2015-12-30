#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

pin24 =24
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin24, GPIO.OUT)

start=time.time()
sleep=0.001
while time.time() < start+10 :
    GPIO.output(pin24, GPIO.HIGH)
    time.sleep(sleep)
    GPIO.output(pin24, GPIO.LOW)
    time.sleep(sleep)

	
GPIO.cleanup()
