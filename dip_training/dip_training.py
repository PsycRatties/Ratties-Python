# DONE NEED TO SET PIN 10 TO PROPER GPIO
import RPi.GPIO as GPIO
import time
import random
import datetime
import os

delay_value = 500  # how fast the audible click is (higher=longer)
interval_upper = 30  # highest time interval that can be selected
interval_lower = 10  # lowest time interval that can be selected
timesToClick = 5  # amount of times the relay should be triggered (default: 10)
runIterations = 2 ## Amount of time the script should loop
runs = 0

# Open File for Logging
file_name = os.getcwd() + '/log' + \
    datetime.datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p') + '.txt'
f = open(file_name, 'w')

GPIO.setmode(GPIO.BOARD)


def setup():
    """
    void function to setup GPIO board for switches.
    Sets input and output of varius pins
    """
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
    global timesToClick, switchCounter2
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
        switchCounter2 = 0

start_time = datetime.datetime.now()
def time_elapsed(delay_time, now_time):
    print(now_time-start_time)
    return True
    
def loop():
    delay_seconds = random.randint(interval_lower, interval_upper) * 1000
    # turn off both LED's on start of script
    GPIO.output(33, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)

    while True:
        if (GPIO.input(40) == GPIO.HIGH and GPIO.input(38) == GPIO.HIGH) or time_elapsed(delay_seconds, datetime.datetime.now()):
            triggerRelay()
        elif (GPIO.input(35) == GPIO.HIGH and GPIO.input(31) == GPIO.HIGH) or time_elapsed(delay_seconds, datetime.datetime.now()):
            triggerRelay()
        delay_seconds = random.randint(interval_lower, interval_upper) * 1000

if __name__ == "__main__":
    # log program start and date and time
    setup()
    f.write("Program Started!")
    f.write(datetime.datetime.now().strftime('%H%M%S'))
    while runIterations > runs:
        start_time = datetime.datetime.now()
        loop()
        runs = runs + 1

    f.close()
