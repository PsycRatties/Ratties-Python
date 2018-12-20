import RPI.GPIO as GPIO
import time
import random
import datetime

delay_value = 500 ## how fast the audible click is (higher=longer)
switchcounter2 = 0
ratio_upper = 10
ratio_lower = 2
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
        switchCounter2 = 0

def void loop():
    switchState2, switchState7 = 0
    lastswitchstate2, lastswitchstate7 = 0

    GPIO.output(33, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)

    vr = random.randint(ratio_lower,ratio_upper)

    if GPIO.input(35) == HIGH:
        GPIO.output(37, GPIO.input(35))
        while switchcounter2 < vr:
            switchState2 = GPIO.input(31)
            if switchState2 != lastswitchstate2 && switchState2 == HIGH:
                switchcounter2++
            time.sleep(.50)
            lastswitchstate7 = switchstate7
        triggerRelay();
        return
    else:
        GPIO.output(33, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)
