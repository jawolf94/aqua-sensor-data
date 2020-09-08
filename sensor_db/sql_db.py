import sqlite3

class SQLDB:

    """Initalize SQLDB class with DB name"""
    def __init__(self):
        self.__db_name = "sensor_data.db"

        self.__create_sensor_tables()

    """Connects to SQLite DB and returns a connection"""
    def __connect(self):
            return sqlite3.connect(self.__db_name)

    """Closes the connection currently open"""
    def __close(self, connection):
           connection.close()

    """ Creates Tables required for storing sensor data"""
    def __create_sensor_tables(self):

        try:
            # Try to establist a connection and make tables

            # Create Thermomether Table
            connection = self.__connect()
            connection.cursor().execute("CREATE TABLE IF NOT EXISTS temperature ([timestamp] timestamp PRIMARY KEY, thermometer_number int, temperature float)")
            connection.commit()

        except Exception as error:
            # Print error is one occurs.
            print(error)

        finally:
            # Always close the connection when complete.
            self.__close(connection)

    """ Stores a temperature reading with the given data"""
    def store_temperature_data(self, timestamp, therm_num, temp):

        try:
            # Get connetion to db
            connection = self.__connect()

            # Set-up string for insertion
            sql_statement = "INSERT INTO temperature(timestamp, thermometer_number, temperature) VALUES (?, ?, ?);"

            # Execute statement
            connection.cursor().execute(sql_statement, (timestamp, therm_num, temp))
            connection.commit()

        except Exception as error:
            # Print error in case of exception
            print(error)

        finally:
            # Always close the connection
            connection.close()
