import wiringpi	
from time import sleep

wiringpi.wiringPiSetupGpio()
outPin=21#change it to whathever pin you want
inPin=20#change it to whathever pin you want
wiringpi.pinMode(outPin,1) #set outPin to 1 (OUTPUT)
wiringpi.pinMode(inPin,1) #set inPin to 0 (INPUT)

while True:
	if wiringpi.digitalRead(inPin)==1:
		wiringpi.digitalWrite(outPin,1)
		sleep(0.2)
	else:
		wiringpi.digitalWrite(outPin,0)
		sleep(0.2)
