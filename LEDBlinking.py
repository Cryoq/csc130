import pineworkslabs.RPi as GPIO
from time import sleep

LED = 16
BUTTON = 25

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    GPIO.output(LED, GPIO.HIGH)
    if GPIO.input(BUTTON) == GPIO.HIGH:
        sleep(.1)
        GPIO.output(LED, GPIO.LOW)
        sleep(.1)
    else:
        sleep(.5)
        GPIO.output(LED, GPIO.LOW)
        sleep(.5)
