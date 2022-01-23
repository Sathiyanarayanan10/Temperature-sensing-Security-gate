import time
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(0)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(servoPIN, True)
	p.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(servoPIN, False)
	p.ChangeDutyCycle(0)

while True:
    temperature=sensor.get_temperature()
    if ((temperature<36) and (temperature>32)):
        SetAngle(90)
        time.sleep(3)
        SetAngle(0)
        GPIO.cleanup()
    elif temperature>36:
        #Have a buzzer beep#
        time.sleep(1)
        GPIO.cleanup()
    else:
        time.sleep(1)
        GPIO.cleanup()

