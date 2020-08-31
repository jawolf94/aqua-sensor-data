import RPi.GPIO as GPIO
import time

"""
    A simple test script to visually verify GPIO functionality using an LED Bulb.
    Important: Script must be run with "sudo" command on Raspberry Pi to execute as expected
 """


# Specify Broadcom (BCM) SOC channel designation & disbale warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# List of invalid GPIO Pin selections
bad_pins = []

# Prompt user for control pin, must be a valid GPIO pin for Raspberry Pi 0
while True:
    try:
        # Get pin number from the user.
        pin_number = int(input("Enter a pin to test: "))
    except ValueError:
        # Catch exception and restart loop if user's selection is invalid
        print("Input must be an integer.")
        continue

    if(pin_number > 1 and pin_number < 27):
        break
    else:
        print("Input must be between 2-26")

# Specify pin 18 as an output pin
GPIO.setup(pin_number,GPIO.OUT)

# Turn LED On/Off unit user end the test
print("Press Ctrl+C at any time to end the test...")
try:
    while True:    
        # Turn on the LED by setting pin 18 to high (3.3v)
        print("LED On.")
        GPIO.output(pin_number,GPIO.HIGH)
        time.sleep(1)

        # Turn off LED by setting pin to Low (0v)
        print("LED Off.")
        GPIO.output(pin_number,GPIO.LOW)
        time.sleep(1)

    except KeyboardInterrupt:
        # Handle Keyboard interupt to gracefully exit
        print("Test Ended.")
        break


