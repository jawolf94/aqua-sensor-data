import os
from time import sleep

# Load drivers for DB18B20
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# File where sensor data is written
therm = '/sys/bus/w1/devices/28-0301a2795434/w1_slave'

""" Reads raw data from w1_driver"""
def read_temp_raw():
    # Open files and get all lines
    f = open(therm, 'r')
    lines = f.readlines()

    # Close file and return lines
    f.close()
    return lines

def read_temp():

    # Read current data in file
    lines = read_temp_raw()

    # Loop until a successful reading occurs
    # The last 3 characters of the first line are 'YES' when reading is successful
    while lines[0].strip[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw()

    # Check if temp data is present
    has_temp = lines[1].find('t=')
    if(has_temp != -1):

        # Get temp from second line starting after 't=' to EOL
        temp = lines[1].strip()[has_temp +2:]

        # Convert raw data to Celcius
        temp = temp/ 1000.0

        # Convert to Fahrenheit
        temp = temp * (9.0/5.0) + 32.0
    
        return temp
