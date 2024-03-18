import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# Load the sales.csv file into a pandas DataFrame
df = pd.read_csv('sales.csv')
matplotlib.use('TkAgg')
# Find the missing values in each column
missing_values = df.isnull().sum()

# find the  values in the product_id column which are present more than once
duplicate_product_ids = df['product_id'].value_counts()[df['product_id'].value_counts() > 1]
print("duplicate ids:",duplicate_product_ids)

# show boxplot of the 'sales_amount' column
df.boxplot(column='sales_amount')
plt.show()


# find outliers in the 'sales_amount' column
Q1 = df['sales_amount'].quantile(0.25)
Q3 = df['sales_amount'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['sales_amount'] < (Q1 - 1.5 * IQR)) | (df['sales_amount'] > (Q3 + 1.5 * IQR))]
print("outliers:",outliers)

# remove the outliers from the 'sales_amount' column
df = df[(df['sales_amount'] >= (Q1 - 1.5 * IQR)) & (df['sales_amount'] <= (Q3 + 1.5 * IQR))]
print(df.shape)

# normalize the 'sales_amount' column
df['sales_amount'] = (df['sales_amount'] - df['sales_amount'].min()) / (df['sales_amount'].max() - df['sales_amount'].min())