# DONE NEED TO SET PIN 10 TO PROPER GPIO
import RPi.GPIO as GPIO
import time
import random
import datetime
import os

delay_value = .500  # how fast the audible click is (higher=longer)
timesToClick = 5  # amount of times the relay should be triggered (default: 10)
switchcounter2 = 0
ratio_upper = 10
ratio_lower = 2
runIterations = 2  # Amount of time the script should loop
runs = 0

file_name = os.getcwd() + '/log' + \
    datetime.datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p') + '.txt'
f = open(file_name, 'w')


def setup():
    """
    function to setup GPIO board for switches.
    Sets input and output of varius pins
    """
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(31, GPIO.IN)  # right switch (spst momentary n.o.) 2
    GPIO.setup(33, GPIO.OUT)  # LED red middle 3
    GPIO.setup(35, GPIO.IN)  # right switch, bottom black (spst) 4
    GPIO.setup(36, GPIO.OUT)  # LED Left Blue 5
    GPIO.setup(37, GPIO.OUT)  # LED Right Green 6
    GPIO.setup(38, GPIO.IN)  # LEft Switch 7
    GPIO.setup(40, GPIO.IN)  # Left Switch 8
    # Need to change
    GPIO.setup(10, GPIO.OUT)  # Relay 10

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
    global timesToClick, switchcounter2
    global delay_value, timesToClick
    GPIO.output(37, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)

    f.write("Relay Triggered!")
    f.write(datetime.datetime.now().strftime('%H%M%S'))

    for x in range(timesToClick):
        GPIO.output(36, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(10, GPIO.HIGH)
        time.sleep(delay_value)  # Note this is is Seconds so might need .500
        GPIO.output(10, GPIO.LOW)
        time.sleep(delay_value)  # Note this is is Seconds so might need .500
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(36, GPIO.LOW)
        switchcounter2 = 0


def loop():
    global switchcounter2
    switchState2 = 0
    switchState7 = 0
    lastswitchstate2 = 0
    lastswitchstate7 = 0

    GPIO.output(33, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)

    vr = random.randint(ratio_lower, ratio_upper)

    if GPIO.input(35) == GPIO.HIGH:
        # log this button being triggered with the time
        f.write("Right Switch Triggered!")
        f.write(datetime.datetime.now().strftime('%H%M%S'))
        GPIO.output(37, GPIO.HIGH)

        while switchcounter2 < vr:
            switchState2 = GPIO.input(31)
            #print(str(GPIO.input(31)) + " | " + str(lastswitchstate2))
            if GPIO.input(31) == GPIO.HIGH and lastswitchstate2 != GPIO.input(31):
                f.write("Switch pressed")
                f.write(datetime.datetime.now().strftime('%H%M%S'))
                switchcounter2 = switchcounter2 + 1
                lastswitchstate2 = GPIO.input(31)
            lastswitchstate2 = GPIO.input(31)
            # time.sleep(.50)
            # lastswitchstate7 = lastswitchstate2
        triggerRelay()
    elif GPIO.input(40) == GPIO.HIGH:
        # log this button being triggered with the time
        f.write("Right Switch Triggered!")
        f.write(datetime.datetime.now().strftime('%H%M%S'))
        GPIO.output(33, GPIO.HIGH)

        while switchcounter2 < vr:
            #print(str(GPIO.input(38)) + " | " + str(lastswitchstate2))
            if GPIO.input(38) == GPIO.HIGH and lastswitchstate2 != GPIO.input(38):
                f.write("Switch pressed")
                f.write(datetime.datetime.now().strftime('%H%M%S'))
                switchcounter2 = switchcounter2 + 1
                lastswitchstate2 = GPIO.input(38)
            lastswitchstate2 = GPIO.input(38)
        triggerRelay()
    else:
        GPIO.output(33, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)


if __name__ == "__main__":
    # log program start and date and time
    setup()
    f.write("Program Started!")
    f.write(datetime.datetime.now().strftime('%H%M%S'))
    while runIterations > runs:
        loop()
        runs = runs + 1

    f.close()
