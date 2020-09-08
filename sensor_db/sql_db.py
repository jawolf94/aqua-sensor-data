import sqlite3

class SQLDB:

    """Initalize SQLDB class with DB name"""
    def __init__(self):
        self.__db_name = "sensor_data.db"
        self.__connection = None

        self.__create_sensor_tables()

    """Connects to SQLite DB and returns a cursor"""
    def __connect(self):
            self.__connection = sqlite3.connect(self.__db_name)
            return self.__connection.cursor()

    """Closes the connection currently open"""
    def __close(self):
        if self.__connection != None: 
            self.__connection.close()
            self.__connection = None

    """ Creates Tables required for storing sensor data"""
    def __create_sensor_tables(self):
        
        try:
            # Try to establist a connection and make tables

            # Create Thermomether Table
            cursor = self.__connect()
            cursor.execute("CREATE TABLE IF NOT EXISTS temperature (timestamp datetime2 PRIMARY KEY, thermometer_number int, temperature float);")
            self.__connection.commit()

        except Exception as error:
            # Print error is one occurs.
            print(error)

        finally:
            # Always close the connection when complete.
            self.__close()

    

    
        

    

