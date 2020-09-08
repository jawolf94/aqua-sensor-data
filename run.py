from datetime import datetime
from time import sleep
from sensor_db import SQLDB
from sensor_data.db18b20 import TempIO

""" Simple function that establishes DB Connection and Collects Sensor Data 
    Currently user must stop execution with ^C
"""

def collect_data():

    print("Starting Data Collection. Press ^C to stop at any time.")

    try:
        # Establish DB Conneciton.
        db = SQLDB()

        # Create TempIO object for temperature readings.
        therm0 = TempIO()

        # Set Thermomerter number to 0. Will be dynamic later
        therm_num = 0

        while True:

            # Get Current time
            time = datetime.now()

            # Read temp data from thermomter
            cur_reading = therm0.read_temp()

            # Store reading in DB
            db.store_temperature_data(time, therm_num, cur_reading)

            #Create string for console printing.
            print_str = "[Thermometer {0} | {1}] The current temperature is: {2:.2f} degrees."
            print_str = print_str.format(therm_num, time, cur_reading)
            print(print_str)

    except BufferError:
        # Catch read error from sensor
        print("Error: Could not read temp data from thermometer")
    except KeyboardInterrupt:
        # Catch keyboard interupt to end program
        print("\nCapture Ended.")
    except Exception as error:
        # Catch all other errors
        print(error)


collect_data()

