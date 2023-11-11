#############################################################################
# author: Alan Dreher
# date: November 10, 2023
# description: Uses Ultrasonic sensor and creates a list using measurements and sorts it
#############################################################################

import pineworkslabs.RPi as GPIO
from time import sleep, time

DEBUG = True
SETTLE_TIME = 2
CALIBRATIONS = 5
CALIBRATION_DELAY = 1
TRIG_DURATION = .00001
SPEED_OF_SOUND = 343

#pin
TRIG = 18
ECHO = 27

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def getTravelTime():
    """
    Gets travel time in sec it take signal to travel sensor to object and back
    """
    GPIO.output(TRIG, GPIO.HIGH)
    sleep(TRIG_DURATION)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO) == GPIO.LOW:
        start = time()
    while GPIO.input(ECHO) == GPIO.HIGH:
        end = time()

    duration = end - start

    if DEBUG:
        print(f"The duration was {duration}")

    return duration


def calculateRawDistance(travelTime):
    """
    Takes in travel time of signal and returns distance(cm) between ultrasonic sensor and other object
    """
    distance = travelTime * SPEED_OF_SOUND
    distance /= 2
    distance *= 100

    if DEBUG:
        print(f"\t\tMeasured {distance} cm")

    return distance

def calibrate():
    """
    Finds and returns correction factor
    """
    print("Calibrating...")
    print("\tPlace the sensor a measured distance away from an object")

    knownDistance = float(input("\tWhat is the measured distance (cm)? "))
    print("\tGetting calibration measurements...")

    runningSum = 0
    for _ in range(CALIBRATIONS):
        travelTime = getTravelTime()
        distance = calculateRawDistance(travelTime)
        runningSum += distance
        print(f"Running sum {runningSum}")
        sleep(CALIBRATION_DELAY)

    averageDistance = runningSum / CALIBRATIONS
    correctionFactor = knownDistance / averageDistance

    if DEBUG:
        print(f"\t\tAverage is {averageDistance}")
        print(f"\t\Correction factor is {correctionFactor}")
        
    print(f"Done Calibrating.\n")
    
    return correctionFactor

def settle():
    """
    Allows sensor to settle
    """
    print(f"Waiting for sensor to settle ({SETTLE_TIME} sec)...")
    GPIO.output(TRIG, GPIO.LOW)
    sleep(SETTLE_TIME)

def bubbleSort(unsorted = list[int]) -> list[int]:
    n = len(unsorted)

    for i in range(n-1):
        for j in range(n-i-1):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

    return unsorted
    
if __name__ == "__main__":
    settle()
    correctionFactor = calibrate()

    input("Press enter to begin...")
    print("Getting measurements: ")
    distanceList = []
    while True:

        print("\tMeasuring")
        travelTime = getTravelTime()
        rawDistance = calculateRawDistance(travelTime)
        trueDistance = rawDistance * correctionFactor
        trueDistance = round(trueDistance, 4)
        print(f"\t\tMeasured: {trueDistance} (cm)")
        distanceList.append(trueDistance)


        response = input("Continue? (Y/n)")
        response = response.lower()

        if response in ["n", "no", "nah"]:
            break

    print(f"The unsorted list is: {distanceList}")
    sortedList = bubbleSort(distanceList)
    print(f" The sorted list is: {sortedList}.")
    print("Done")
    GPIO.cleanup()
