import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
outPin=21#change it to whathever pin you want
inPin=20
GPIO.setup(outPin,GPIO.OUT)#you can add initial state with ,initial=GPIO.HIGH
GPIO.setup(inPin,GPIO.IN)#you can add initial state with ,initial=GPIO.HIGH

while True:
	if GPIO.input(inPin):
		GPIO.output(outPin,GPIO.HIGH)
		sleep(0.5)
	else:
		GPIO.output(outPin,GPIO.LOW)
		sleep(0.5)
