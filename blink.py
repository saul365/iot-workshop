import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
pin=21#change it to whathever pin you want
GPIO.setup(pin,GPIO.OUT)#you can add initial state with ,initial=GPIO.HIGH

while True:
	sleep(0.5)
	GPIO.output(pin,GPIO.HIGH)
	sleep(0.5)
	GPIO.output(pin,GPIO.LOW)
	
