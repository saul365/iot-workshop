import wiringpi
from time import sleep


wiringpi.wiringPiSetupGpio()
pin=21#change it to whathever pin you want
wiringpi.pinMode(pin,1) #set pin 21 to 1 (OUTPUT)
while True:
	sleep(0.5)
	wiringpi.digitalWrite(21,1)
	sleep(0.5)
	wiringpi.digitalWrite(21,0)
