from sensor_data.db18b20 import TempIO
from time import sleep

# Creates new instance of TempIO Class.
therm = TempIO()

# Loop until user ends the program.
try:
    while True:
        try:    
            # Read & Print temp data from thermometer.
            print(therm.read_temp)
        except BufferError:
            print("Error: Could not read tempurature data from the thermometer.")

        # Sleep before next read.
        sleep(2)

except KeyboardInterrupt:
    # Gracefully end the test if user ends the script.
    print("Test Ended.")

