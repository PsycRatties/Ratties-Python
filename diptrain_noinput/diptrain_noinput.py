#DONE ANYTHING WITH GPIO 10 NEEDS TO BE SET TO PROPER GPIO 
import RPI.GPIO as GPIO
import time
import random
import datetime


GPIO.setmode(GPIO.BOARD)

delay_value = 500 ## how fast the audible click is (higher=longer)
interval_upper = 30 ## highest time interval that can be selected
interval_lower = 10 ## lowest time interval that can be selected
timesToClick = 5 ## amount of times the relay should be triggered (default: 10)
## Open File for Logging 
f = open('log.txt','w')



def void setup():
    """
    void function to setup GPIO board for switches.
    Sets input and output of varius pins
    """
    GPIO.setup(31, GPIO.IN) ## right switch (spst momentary n.o.) 2
    GPIO.setup(33, GPIO.OUT) ## LED red middle 3
    GPIO.setup(35, GPIO.IN) ## right switch, bottom black (spst) 4
    GPIO.setup(36, GPIO.OUT) ## LED Left Blue 5
    GPIO.setup(37, GPIO.OUT) ## LED Right Green 6
    GPIO.setup(38, GPIO.IN) ## LEft Switch 7
    GPIO.setup(40, GPIO.IN) ## Left Switch 8
    #Need to change
    GPIO.setup(10, GPIO.OUT) ## Relay 10
    delay_seconds = delay_seconds * 1000

def void triggerRelay():
    """
    Void Function to triggerRelay to start.
    Will turn on and off Pins 5 & 10 with a delay
    Uses 'delay_value', 'timesToClick'

    """
    GPIO.output(37, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)

    for x in 10:
        GPIO.output(36, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(10, GPIO.HIGH)
        time.sleep(delay_value) ## Note this is is Seconds so might need .500
        GPIO.output(10, GPIO.LOW)
        time.sleep(delay_value) ## Note this is is Seconds so might need .500
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(36, GPIO.LOW)
        switchCounter2 = 0


def void loop():
    delay_seconds = random.randint(interval_lower,interval_upper) * 1000

    time.sleep(delay_seconds)
    triggerRelay()
