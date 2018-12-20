#DONE NEED TO SET PIN 10
import RPI.GPIO as GPIO
import time
import random
import datetime

delay_value = 500 ## how fast the audible click is (higher=longer)
fr = 5
interval_upper = 10
interval_lower = 2
## Open File for Logging 
f = open('log.txt','w')

GPIO.setmode(GPIO.BOARD)

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


def void triggerRelay():
    """
    Void Function to triggerRelay to start.
    Will turn on and off Pins 5 & 10 with a delay
    Uses 'delay_value', 'timesToClick'

    """
    GPIO.output(37, GPIO.LOW) ## Turn off GREEN Light
    GPIO.output(33, GPIO.LOW) ## Turn off RED Light

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


def void loop():
    hasRun = False
    delay_seconds = random.randint(interval_lower,interval_upper) * 1000
    GPIO.output(33, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    if GPIO.input(35) == HIGH:
        GPIO.output(37, GPIO.input(35))
        time.sleep(delay_seconds)
        while !hasRun:
            if GPIO.INPUT(31) == HIGH:
                hasRun = True
                triggerRelay()
    elif GPIO.input(40) == HIGH:
        GPIO.output(33, GPIO.input(40))
        time.sleep(delay_seconds)
        while !hasRun:
            if GPIO.input(38) == HIGH:
                hasRun = True
                triggerRelay()
        else:
            GPIO.output(33, GPIO.LOW)
            GPIO.output(37, GPIO.LOW)
