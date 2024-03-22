# SalesOutlook_View.py

import logging
from SalesOutlook_Model import Database
from SalesOutlook_Query import DatabaseQueries

host = 'localhost'
user = 'root'
password = 'Root123@'
database_name = 'Sales_Outlook'

logging.basicConfig(filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class View:
    def __init__(self, database_name):
        self.db = Database(host, user, password, database_name)
        self.queries = DatabaseQueries(self.db)

    def display_total_sales_per_category(self):
        try:
            df = self.queries.total_sales_per_category()
            print("Total sales amount for each product category:")
            print(df)
            logging.info("Displayed total sales per category")
        except Exception as e:
            logging.error(f"Error displaying total sales per category: {e}")

    def display_join_sales_and_product_info(self):
        try:
            df = self.queries.join_sales_and_product_info()
            print("\nSales data along with product information:")
            print(df)
            logging.info("Displayed joined sales and product info")
        except Exception as e:
            logging.error(f"Error displaying joined sales and product info: {e}")

    def customers_highest_purchase(self):
        try:
            df = self.queries.customers_highest_purchase()
            print("\nCustomers who made the highest purchase:")
            print(df)
            logging.info("Displayed customers highest purchase")
        except Exception as e:
            logging.error(f"Error displaying customers highest purchase: {e}")

    def average_sales_by_month_year(self):
        try:
            df = self.queries.average_sales_by_month_year()
            print("\nAverage sales by month year:")
            print(df)
            logging.info("Displayed average sales by month year")
        except Exception as e:
            logging.error(f"Error displaying average sales by month year: {e}")

    def top_selling_products_by_region(self):
        try:
            df = self.queries.top_selling_products_by_region()
            print("\nTop selling products by region:")
            print(df)
            logging.info("Displayed top selling products by region")
        except Exception as e:
            logging.error(f"Top selling products by region: {e}")

if __name__ == "__main__":
    logging.info("Starting program")

    view = View(database_name)
    view.display_total_sales_per_category()
    view.display_join_sales_and_product_info()
    view.average_sales_by_month_year()
    view.customers_highest_purchase()
    view.top_selling_products_by_region()

    logging.info("Program finished")