# SalesOutlook_Query.py

import logging
from SalesOutlook_Model import Database
import pandas as pd

class DatabaseQueries:
    def __init__(self, database):
        self.database = database

    def execute_query(self, query):
        try:
            with self.database as db:  # Ensure proper usage of context manager
                db.cursor.execute(query)
                result = db.cursor.fetchall()
                return result
        except Exception as e:
            logging.error(f"Error executing query: {e}")
            return None

    # 1. Write a SQL query to retrieve total sales amount for each product category.
    def total_sales_per_category(self):
        query = '''
            SELECT Product_Category, SUM(Sales) AS Total_Sales 
            FROM Sales
            JOIN Products ON Sales.Product_ID = Products.Product_ID
            GROUP BY Product_Category;
            '''
        result = self.execute_query(query)
        df = pd.DataFrame(result, columns=['Product_Category', 'Total_Sales'])
        return df

    # 2. Perform a join operation to retrieve sales data along with product information.
    def join_sales_and_product_info(self):
        query = '''
            SELECT Sales.*, Products.Product_Name, Products.Product_Category, Products.Unit_Price 
            FROM Sales
            JOIN Products ON Sales.Product_ID = Products.Product_ID;
            '''
        result = self.execute_query(query)
        df = pd.DataFrame(result, columns=['Sales_ID', 'Product_ID', 'Customer_ID', 'Sales', 'Order_Date', 'Region_ID',
                                           'Product_Name', 'Product_Category', 'Unit_Price'])
        return df

    # 3. Write a subquery to find customers who made the highest purchase.
    def customers_highest_purchase(self):
        query = '''
            SELECT Customer_ID, Customer_Name, Email_ID, Address 
            FROM Customers 
            WHERE Customer_ID = (
                SELECT Customer_ID 
                FROM Sales 
                GROUP BY Customer_ID 
                ORDER BY SUM(Sales) DESC 
                LIMIT 1
            );
        '''
        result = self.execute_query(query)
        df = pd.DataFrame(result, columns=['Customer_ID', 'Customer_Name', 'Email_ID', 'Address'])
        return df

    # 4. Use the GROUP BY clause to calculate the average sales amount by month and year.
    def average_sales_by_month_year(self):
        query = '''
            SELECT YEAR(Order_Date) AS Year, MONTH(Order_Date) AS Month, AVG(Sales) AS Average_Sales 
            FROM Sales
            GROUP BY Year, Month;
            '''
        result = self.execute_query(query)
        df = pd.DataFrame(result, columns=['Year', 'Month', 'Average_Sales'])
        df['Year_Month'] = df['Year'].astype(str) + '-' + df['Month'].astype(str).str.zfill(2)
        df.drop(['Year', 'Month'], axis=1, inplace=True)
        df.sort_values(by='Year_Month', inplace=True)
        return df

    # 5. Write a complex SQL query to find the top-selling products by region.
    def top_selling_products_by_region(self):
        query = '''
            SELECT Regions.Region, Products.Product_Name, Products.Product_Category, SUM(Sales) AS Total_Sales 
            FROM Sales
            JOIN Regions ON Sales.Region_ID = Regions.Region_ID
            JOIN Products ON Sales.Product_ID = Products.Product_ID
            GROUP BY Regions.Region, Products.Product_Name, Products.Product_Category
            ORDER BY Regions.Region, Total_Sales DESC;
            '''
        result = self.execute_query(query)
        df = pd.DataFrame(result, columns=['Region', 'Product_Name', 'Product_Category', 'Total_Sales'])
        return df