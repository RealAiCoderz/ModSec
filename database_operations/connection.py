import logger as log
import mysql.connector
#------------------------------importing complete-----------------------------------

class Connection:
    def make_connection(self, db_name=None):
        try:
            conn = mysql.connector.connect(
            host = "localhost",
            user = "<username>",
            password = "<password>",
            database = db_name
            )
        except Exception as e:
            print(type(e).__name__, e)
            log.make_entry("ERROR: {}: {}".format(type(e).__name__, str(e)))
        else:
            cursor = conn.cursor()
            return (conn, cursor)   # return connection and cursor objects
