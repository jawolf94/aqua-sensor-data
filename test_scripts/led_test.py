import RPi.GPIO as GPIO
import time

"""
    A simple test script to visually verify GPIO functionality using an LED Bulb.
    Important: Script must be run with "sudo" command on Raspberry Pi to execute as expected
 """

# Specify Broadcom (BCM) SOC channel designation
GPIO.setmode(GPIO.BCM)

# Disable warnings 
GPIO.setwarnings(False)

# Specify pin 18 as an output pin
GPIO.setup(18,GPIO.OUT)

# Turn on the LED by setting pin 18 to high (3.3v)
print("LED On.")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)

# Turn off LED by setting pin to Low (0v)
print("LED Off.")
GPIO.output(18,GPIO.LOW)

