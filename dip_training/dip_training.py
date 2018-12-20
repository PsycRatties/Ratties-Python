#Done ANYTHING GPIO 10 NEEDS TO BE SET TO PROPER GPIO NOT ARDUINO 
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

#     GPIO.setup(2, GPIO.IN) ## right switch (spst momentary n.o.)
#     GPIO.setup(3, GPIO.OUT) ## LED red middle
#     GPIO.setup(4, GPIO.IN) ## right switch, bottom black (spst)
#     GPIO.setup(5, GPIO.OUT) ## LED Left Blue
#     GPIO.setup(6, GPIO.OUT) ## LED Right Green
#     GPIO.setup(7, GPIO.IN) ## LEft Switch
#     GPIO.setup(8, GPIO.IN) ## Left Switch
#     GPIO.setup(10, GPIO.OUT) ## Relay


def void triggerRelay():
    """
    Void Function to triggerRelay to start.
    Will turn on and off Pins 5 & 10 with a delay
    Uses 'delay_value', 'timesToClick'

    """
    GPIO.output(37, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)

    for x in timesToClick:
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
    delay_seconds = random.randint(interval_lower,interval_upper) * 1000 
    ## turn off both LED's on start of script
    GPIO.output(33,GPIO.LOW)
    GPIO.output(37,GPIO.LOW)
    state = GPIO.input(40)

    while True:
        time.sleep(delay_seconds)
        if state == HIGH:
            triggerRelay()
        else:
            break
        delay_seconds = random.randint(interval_lower,interval_upper) * 1000

    ## Might want this instead?
    while  state == 40:
        triggerRelay()
    else:
        return
