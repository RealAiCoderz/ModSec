#SalesOutlook_Controller.py
import mysql.connector as mysql
import pandas as pd
import logging
from SalesOutlook_Model import Database

host = 'localhost'
user = 'root'
password = 'Root123@'
database_name = 'Sales_Outlook'

logging.basicConfig(filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class Controller:
    def __init__(self, host, user, password, database_name):
        self.db = Database(host, user, password, database_name)

    def initialize_database(self):
        try:
            self.db.connect()
            self.create_tables()
            self.populate_tables_from_csv()
        except Exception as e:
            logging.error(f"Error initializing database: {e}")
        finally:
            self.db.disconnect()

    def create_tables(self):
        create_queries = [
            '''
            CREATE TABLE IF NOT EXISTS Customers (
                Customer_ID VARCHAR(255) PRIMARY KEY,
                Customer_Name VARCHAR(255),
                Email_ID VARCHAR(255),
                Address VARCHAR(255)
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS Products (
                Product_ID VARCHAR(255) PRIMARY KEY,
                Product_Name VARCHAR(255),
                Product_Category VARCHAR(255),
                Unit_Price DECIMAL(10, 2)
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS Regions (
                Region VARCHAR(255),
                Region_ID INT PRIMARY KEY
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS Sales (
                Sales_ID INT PRIMARY KEY,
                Product_ID VARCHAR(255),
                Customer_ID VARCHAR(255),
                Sales DECIMAL(10, 2),
                Order_Date DATE,
                Region_ID INT,
                FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
                FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID),
                FOREIGN KEY (Region_ID) REFERENCES Regions(Region_ID)
            );
            '''
        ]

        conn = self.db.conn
        cursor = self.db.cursor
        try:
            for query in create_queries:
                cursor.execute(query)
                logging.info(f"Table created: {query.split()[3]}")
        except mysql.Error as err:
            logging.error(f"Error creating table: {err}")

    def populate_tables_from_csv(self):
        try:
            sales_data = pd.read_csv("/Users/shalinitandon/Sales_Outlook/AI Bootcamp/csv_Files/sales_table.csv",
                                     encoding='latin1', index_col=False)
            customer_data = pd.read_csv("/Users/shalinitandon/Sales_Outlook/AI Bootcamp/csv_Files/customers_table.csv",
                                        encoding='latin1', index_col=False)
            products_data = pd.read_csv("/Users/shalinitandon/Sales_Outlook/AI Bootcamp/csv_Files/products_table.csv",
                                        encoding='latin1', index_col=False)
            regions_data = pd.read_csv("/Users/shalinitandon/Sales_Outlook/AI Bootcamp/csv_Files/regions_table.csv",
                                       encoding='latin1', index_col=False)

            conn = self.db.conn
            cursor = self.db.cursor

            for i, row in customer_data.iterrows():
                sql = "INSERT INTO Customers (Customer_ID, Customer_Name, Email_ID, Address) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (row['Customer ID'], row['Customer Name'], row['Email ID'], row['Address']))
            logging.info("Records inserted into Customers")

            for i, row in products_data.iterrows():
                sql = "INSERT INTO Products VALUES (%s,%s,%s,%s)"
                cursor.execute(sql,
                               (row['Product ID'], row['Product Name'], row['Product Category'], row['Unit Price']))
            logging.info("Records inserted into Products")

            for i, row in regions_data.iterrows():
                sql = "INSERT INTO Regions VALUES (%s,%s)"
                cursor.execute(sql, (row['Region'], row['Region ID']))
            logging.info("Records inserted into Regions")

            for i, row in sales_data.iterrows():
                order_date = pd.to_datetime(row['Order Date'], format='%m/%d/%Y').strftime('%Y-%m-%d')
                sql = "INSERT INTO Sales VALUES (%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (
                    row['Sales ID'], row['Product ID'], row['Customer ID'], row['Sales'], order_date, row['Region ID']))
                logging.info("Record inserted into Sales")

            conn.commit()
        except mysql.Error as err:
            logging.error(f"Error inserting data: {err}")
        except FileNotFoundError as fnf_err:
            logging.error(f"File not found: {fnf_err}")
        except Exception as e:
            logging.error(f"Error: {e}")


if __name__ == "__main__":
    logging.info("Starting Program")
    controller = Controller(host, user, password, database_name)
    controller.initialize_database()
    logging.info("Finished Program")
