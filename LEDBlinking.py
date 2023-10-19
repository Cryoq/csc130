import pineworkslabs.RPi as GPIO
from time import sleep

LED = 16
BUTTON = 25
GPIO.setmode(GPIO.LE_POTATO_LOOKUP)
#Sets up the LED and BUTTON
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Runs loop forever 
while True:
    #Turns on LED
    GPIO.output(LED, GPIO.HIGH)
    #If Pressed, blinks for .1 seconds
    if GPIO.input(BUTTON) == GPIO.HIGH:
        sleep(.1)
        GPIO.output(LED, GPIO.LOW)
        sleep(.1)
    #If NOT Pressed, blinks for .5 seconds
    else:
        sleep(.5)
        GPIO.output(LED, GPIO.LOW)
        sleep(.5)
