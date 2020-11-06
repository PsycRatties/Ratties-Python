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
    GPIO.setup(31, GPIO.IN) ## right switch (spst momentary n.o.) 2
    GPIO.setup(33, GPIO.OUT) ## LED red middle 3
    GPIO.setup(35, GPIO.IN) ## right switch, bottom black (spst) 4
    GPIO.setup(36, GPIO.OUT) ## LED Left Blue 5
    GPIO.setup(37, GPIO.OUT) ## LED Right Green 6
    GPIO.setup(38, GPIO.IN) ## LEft Switch 7
    GPIO.setup(40, GPIO.IN) ## Left Switch 8
    #Need to change
    GPIO.setup(10, GPIO.OUT) ## Relay 10

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
    global delay_value, timesToClick
    GPIO.output(37, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)

    for x in range(timesToClick):
        GPIO.output(36, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(10, GPIO.HIGH)
        time.sleep(delay_value) ## Note this is is Seconds so might need .500
        GPIO.output(10, GPIO.LOW)
        #time.sleep(delay_value) ## Note this is is Seconds so might need .500
        #GPIO.output(10, GPIO.HIGH)
        #GPIO.output(10, GPIO.LOW)
        GPIO.output(36, GPIO.LOW)
        switchcounter2 = 0

def loop():
    global fr, switchCounter2
    switchState2 = 0
    switchState7 = 0
    lastswitchstate2 = 0
    lastswitchstate7 = 0

    GPIO.output(33, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)

    print("starting")

    if GPIO.input(35) == GPIO.HIGH:
        # log this button being triggered with the time
        f.write("Right Switch Triggered!")
        f.write(datetime.datetime.now().strftime('%H%M%S'))
        GPIO.output(37, GPIO.HIGH)

        while switchCounter2 < fr:
            if GPIO.input(31) == GPIO.HIGH and lastswitchstate2 != GPIO.input(31):
                switchCounter2 = switchCounter2 + 1
                lastswitchstate2 = GPIO.input(31)
            lastswitchstate2 = GPIO.input(31)

        triggerRelay()
    elif GPIO.input(40) == GPIO.HIGH:
        # log this button being triggered with the time
        f.write("Left Switch Triggered!")
        f.write(datetime.datetime.now().strftime('%H%M%S'))
        GPIO.output(33, GPIO.HIGH)

        while switchCounter2 < fr:
            if GPIO.input(38) == GPIO.HIGH and lastswitchstate2 != GPIO.input(38):
                switchCounter2 = switchCounter2 + 1
                lastswitchstate2 = GPIO.input(38)
            lastswitchstate2 = GPIO.input(38)

        triggerRelay()
    else:
        GPIO.output(33, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)

if __name__== "__main__":
  ## log program start and date and time
  setup()
  f.write("Program Started!")
  f.write(datetime.datetime.now().strftime('%H%M%S'))
  while runs < runIterations:
      runs = runs + 1
      loop()

  f.close()
