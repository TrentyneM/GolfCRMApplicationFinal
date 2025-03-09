# FINAL PROJECT SDEV220

import mysql.connector   # MySQL Database Management Library

database = mysql.connector.connect(

        host = 'localhost',
        user = 'root',
        passwd = '32551766767asdf',

        )

# Our cursor object to navigate the database
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE golfco")

# Printing a test message.
print("All Done!")
