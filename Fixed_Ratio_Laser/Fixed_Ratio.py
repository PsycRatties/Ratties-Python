#DONE NEED TO SET PIN 10 TO PROPER GPIO 
import RPi.GPIO as GPIO
import time, random, datetime, os

delay_value = .500 ## how fast the audible click is (higher=longer)
fr = 5
switchCounter2 = 0
timesToClick = 10
runIterations = 2 ## Amount of time the script should loop
runs = 0

## Open File for Logging 
file_name = os.getcwd() + '/log' + datetime.datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p') + '.txt'
f = open(file_name,'w')

GPIO.setmode(GPIO.BOARD)

def setup():
    """
    void function to setup GPIO board for switches.
    Sets input and output of varius pins
    """
    GPIO.setup(7, GPIO.OUT) ## House light LED
    GPIO.setup(31, GPIO.IN) ## right switch (spst momentary n.o.) 2
    GPIO.setup(33, GPIO.OUT) ## LED red middle 3
    GPIO.setup(35, GPIO.IN) ## right switch, bottom black (spst) 4
    GPIO.setup(36, GPIO.OUT) ## LED Left Blue 5
    GPIO.setup(37, GPIO.OUT) ## LED Right Green 6
    GPIO.setup(38, GPIO.IN) ## LEft Switch 7
    GPIO.setup(40, GPIO.IN) ## Left Switch 8
    #Need to change
    GPIO.setup(10, GPIO.OUT) ## Relay 10

    GPIO.output(7, GPIO.HIGH)
    GPIO.output(33, GPIO.LOW)
    GPIO.output(36, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)

def triggerRelay():
    """
    Void Function to triggerRelay to start.
    Will turn on and off Pins 5 & 10 with a delay
    Uses 'delay_value', 'timesToClick'

    """
    global timesToClick, switchCounter2
    global delay_value, timesToClick
    GPIO.output(37, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)

    f.write("Relay Triggered!")
    f.write(datetime.datetime.now().strftime('%H%M%S')) 
    
    laser_state = GPIO.LOW
    max_time = 0.500
    
    while laser_state == GPIO.LOW:
        if GPIO.input(31) == GPIO.HIGH: laser_state = GPIO.HIGH
        GPIO.output(36, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(10, GPIO.HIGH)
        start_time = time.time()
        while (time.time() - start_time) < max_time:
            if GPIO.input(31) == GPIO.HIGH: laser_state = GPIO.HIGH
        GPIO.output(10, GPIO.LOW)
        start_time = time.time()
        while (time.time() - start_time) < max_time:
            if GPIO.input(31) == GPIO.HIGH: laser_state = GPIO.HIGH
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(36, GPIO.LOW)
        laser_state = GPIO.input(31)
    switchCounter2 = 0

def loop():
    global fr, switchCounter2
    lastswitchstate2 = 0

    GPIO.output(33, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)

    if GPIO.input(35) == GPIO.HIGH:
        # log this button being triggered with the time
        f.write("Left Switch Triggered!")
        f.write(datetime.datetime.now().strftime('%H%M%S'))
        GPIO.output(37, GPIO.HIGH)

        while switchCounter2 < fr:
            print(str(GPIO.input(31)) + " | " + str(lastswitchstate2))
            if GPIO.input(31) == GPIO.HIGH and lastswitchstate2 != GPIO.input(31):
                f.write("Switch pressed")
                f.write(datetime.datetime.now().strftime('%H%M%S'))
                switchCounter2 = switchCounter2 + 1
                lastswitchstate2 = GPIO.input(31)
            lastswitchstate2 = GPIO.input(31)

        triggerRelay()
    elif GPIO.input(40) == GPIO.HIGH:
        # log this button being triggered with the time
        f.write("Right Switch Triggered!")
        f.write(datetime.datetime.now().strftime('%H%M%S'))
        GPIO.output(33, GPIO.HIGH)

        while switchCounter2 < fr:
            print(str(GPIO.input(38)) + " | " + str(lastswitchstate2))
            if GPIO.input(38) == GPIO.HIGH and lastswitchstate2 != GPIO.input(38):
                f.write("Switch pressed")
                f.write(datetime.datetime.now().strftime('%H%M%S'))
                switchCounter2 = switchCounter2 + 1
                lastswitchstate2 = GPIO.input(38)
            lastswitchstate2 = GPIO.input(38)

        triggerRelay()
    else:
        GPIO.output(33, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)
    
    f.write("Program Finished!")
    f.write(datetime.datetime.now().strftime('%H%M%S'))

if __name__== "__main__":
    ## log program start and date and time
    setup()
    f.write("Program Started!")
    f.write(datetime.datetime.now().strftime('%H%M%S'))
    while runIterations > runs:
        loop()
        runs = runs + 1
    GPIO.output(7, GPIO.LOW)
    f.close()
