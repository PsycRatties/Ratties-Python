# DONE NEED TO SET PIN 10 TO PROPER GPIO
# G2G
import RPi.GPIO as GPIO
import time
import random
import datetime
import os
import csv
import sys

delay_value = .500  # how fast the audible click is (higher=longer)
interval_upper = 30  # highest time interval that can be selected
interval_lower = 10  # lowest time interval that can be selected
timesToClick = 5  # amount of times the relay should be triggered (default: 10)
runs = 0

file_name = os.getcwd() + '/log' + \
    datetime.datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p') + '.txt'
f = open(file_name, 'w')

sleep_times = list()
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

    try:
        with open('time.csv', newline='') as file:
            reader = csv.reader(file)
            sleep_times = list(reader)
    except:
        sys.exit("COULD NOT FILD time.csv")


def triggerRelay():
    """
    Void Function to triggerRelay to start.
    Will turn on and off Pins 5 & 10 with a delay
    Uses 'delay_value', 'timesToClick'

    """
    global timesToClick
    global delay_value, timesToClick
    GPIO.output(37, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)

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

sleep_pos = 0
def loop():
    global sleep_pos, sleep_times
    hasRun = False 
    GPIO.output(33, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    print("started loop")

    time_to_sleep = sleep_times[sleep_pos]
    f.write("Delay input time: " + str(time_to_sleep))

    if (GPIO.input(35) == GPIO.HIGH):
        # log this button being triggered with the time
        f.write("Right Switch Triggered!")
        f.write(datetime.datetime.now().strftime('%H%M%S'))
        GPIO.output(37, GPIO.HIGH)

        time.sleep(time_to_sleep)

        while not hasRun:
            if GPIO.input(31) == GPIO.HIGH:
                # log that it is triggering relay with the time
                f.write("Relay Triggered!")
                f.write(datetime.datetime.now().strftime('%H%M%S'))
                hasRun = True
                triggerRelay()
                # log that the program is done with the time
                f.write("Program Finished!")
                f.write(datetime.datetime.now().strftime('%H%M%S'))
                break
    elif (GPIO.input(40) == GPIO.HIGH):
        # log this button being triggered with the time
        f.write("Left Switch Triggered!")
        f.write(datetime.datetime.now().strftime('%H%M%S'))
        GPIO.output(33, GPIO.HIGH)

        time.sleep(time_to_sleep)

        while not hasRun:
            if GPIO.input(38) == GPIO.HIGH:
                # log that it is triggering relay with the time
                f.write("Relay Triggered!")
                f.write(datetime.datetime.now().strftime('%H%M%S'))
                hasRun = True
                triggerRelay()

                # log that the program is done with the time
                f.write("Program Finished!")
                f.write(datetime.datetime.now().strftime('%H%M%S'))
                break
    sleep_pos = sleep_pos + 1


if __name__ == "__main__":
    global sleep_times
    # log program start and date and time
    setup()
    f.write("Program Started!")
    f.write(datetime.datetime.now().strftime('%H%M%S'))
    print(sleep_times)
    while len(sleep_times) > runs:
        loop()
        runs = runs + 1

    f.close()
