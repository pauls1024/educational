import RPi.GPIO as GPIO
import time

pin4 =4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin4, GPIO.OUT)
while True:
    GPIO.output(pin4, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin4, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()
