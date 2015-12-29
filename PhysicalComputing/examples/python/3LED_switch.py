import RPi.GPIO as GPIO
import time

pin4 =4
pin17 =17
pin23 =23
pin25 =25
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin4, GPIO.OUT)
GPIO.setup(pin17, GPIO.OUT)
GPIO.setup(pin23, GPIO.OUT)
GPIO.setup(pin25, GPIO.IN, pull_up_down=GPIO.PUD_UP)



while True:
    GPIO.output(pin4, GPIO.HIGH)
    GPIO.output(pin17, GPIO.HIGH)
    GPIO.output(pin23, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin4, GPIO.LOW)
    GPIO.output(pin17, GPIO.LOW)
    GPIO.output(pin23, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()
