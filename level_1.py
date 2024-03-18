import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('sales.csv')

# Display 5 rows from the DataFrame
print(df.head(5))

# Display the number of rows and columns in the DataFrame
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# mean, median, and mode of the 'sales' column
print("Mean:", df['sales_amount'].mean())
print("Median:", df['sales_amount'].median())
print("Mode:", df['sales_amount'].mode()[0])

# number of unique product_id
print("Number of unique product_id:", df['product_id'].nunique())
