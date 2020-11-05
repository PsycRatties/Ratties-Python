#DONE NEED TO SET PIN 10 TO PROPER GPIO 
#G2G
import RPI.GPIO as GPIO
import time
import random
import datetime

delay_value = 500 ## how fast the audible click is (higher=longer)
interval_upper = 30 ## highest time interval that can be selected
interval_lower = 10 ## lowest time interval that can be selected
timesToClick = 5 ## amount of times the relay should be triggered (default: 10)
delay_seconds = 10
## Open File for Logging 
f = open('log.txt','w')



GPIO.setmode(GPIO.BOARD)


def setup():
    """
    function to setup GPIO board for switches.
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
        time.sleep(delay_value) ## Note this is is Seconds so might need .500
        GPIO.output(10, GPIO.LOW)
        time.sleep(delay_value) ## Note this is is Seconds so might need .500
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(36, GPIO.LOW)
        switchcounter2 = 0

def loop():
    hasRun = False
    GPIO.output(33, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)

    if (GPIO.input(35) == HIGH):
        # log this button being triggered with the time
        f.write("Right Switch Triggered!")
        f.write(datetime.datetime.now())    
        GPIO.output(37, GPIO.HIGH)
        while not hasRun:
            if GPIO.input(31) == HIGH:
                # log that it is triggering relay with the time
                f.write("Relay Triggered!")
                f.write(datetime.datetime.now())    
                hasRun = True
                triggerRelay()    
                # log that the program is done with the time
                f.write("Program Finished!")
                f.write(datetime.datetime.now())
                break
    elif (GPIO.input(40) == HIGH):
        # log this button being triggered with the time
        f.write("Left Switch Triggered!")
        f.write(datetime.datetime.now()) 
        GPIO.output(33, GPIO.HIGH)
        while not hasRun:
            if GPIO.input(38) == HIGH:
                # log that it is triggering relay with the time
                f.write("Relay Triggered!")
                f.write(datetime.datetime.now()) 
                hasRun = True
                triggerRelay()
                
                # log that the program is done with the time
                f.write("Program Finished!")
                f.write(datetime.datetime.now())
                break

if __name__== "__main__":
  while true:
      ## log program start and date and time
      f.write("Program Started!")
      f.write(datetime.datetime.now())    
      loop()
      f.close()
      break
