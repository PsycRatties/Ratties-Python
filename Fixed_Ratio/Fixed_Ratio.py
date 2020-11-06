#DONE NEED TO SET PIN 10 TO PROPER GPIO 
import RPi.GPIO as GPIO
import time, random, datetime

## Open File for Logging 
file_name = os.getcwd() + '/log' + datetime.datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p') + '.txt'
f = open(file_name,'w')


delay_value = 500 ## how fast the audible click is (higher=longer)
fr = 5
switchCounter2 = 0

GPIO.setmode(GPIO.BOARD)

def setup():
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

def triggerRelay():
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
        time.sleep(delay_value) ## Note this is Seconds so might need .500
        GPIO.output(10, GPIO.LOW)
        time.sleep(delay_value) ## Note this is Seconds so might need .500
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(36, GPIO.LOW)
        switchcounter2 = 0

def loop():
    switchState2, switchState7 = 0
    lastswitchstate2, lastswitchstate7 = 0

    GPIO.output(33, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)

    if GPIO.input(35) == GPIO.HIGH:
        GPIO.output(37, GPIO.input(35))
        while switchCounter2 < fr:
            if lastswitchstate2 != lastswitchstate2:
                switchState2 = GPIO.input(31)
                time.sleep(.50)
                lastswitchstate2 = switchState2
                triggerRelay()
                return
    elif GPIO.input(40) == GPIO.HIGH:
        GPIO.output(33,GPIO.input(40))
        while switchCounter2 < fr:
            switchState7 = GPIO.input(38)
            if switchState7 != lastswitchstate7 and switchState7 == GPIO.HIGH:
                switchCounter2++
            time.sleep(.5)
            lastswitchstate7 = switchState7
        triggerRelay()
        return
    else:
        GPIO.output(33, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)
