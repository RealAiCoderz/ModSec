# SalesOutlook_Model.py

import mysql.connector as mysql
import logging

class Database:
    def __init__(self, host, user, password, database_name):
        self.host = host
        self.user = user
        self.password = password
        self.database_name = database_name
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connect(host=self.host, user=self.user, password=self.password, database=self.database_name)
            self.cursor = self.conn.cursor()
            logging.info("Connected to the database")
        except mysql.Error as err:
            logging.error(f"Error connecting to the database: {err}")
            raise  # Raise the exception to indicate failure to connect

    def disconnect(self):
        if self.conn is not None and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            logging.info("Disconnected from the database")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()