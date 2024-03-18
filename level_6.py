import numpy as np
# level-6
# q1: Use Numpy to calculate the mean, median, and standard deviation of the sales data

# Load sales data from CSV file
sales_data = np.genfromtxt('sales.csv', delimiter=',',usecols=(3,))

# Calculate mean, median, and standard deviation
mean_sales = np.mean(sales_data)
median_sales = np.median(sales_data)
std_dev_sales = np.std(sales_data)

print("Mean:", mean_sales)
print("Median:", median_sales)
print("Standard Deviation:", std_dev_sales)
# -------------------------------------------------------------------------
# q2:Perform element-wise arithmetic operations on the sales data (e.g., addition, subtraction,
# multiplication).
add_value = 100
subtract_value = 50
multiply_value = 2
divide_value = 5

# Perform element-wise arithmetic operations
sales_data_addition = sales_data + add_value
sales_data_subtraction = sales_data - subtract_value
sales_data_multiplication = sales_data * multiply_value
sales_data_division = sales_data / divide_value

# Print the results
print("Sales data after addition:", sales_data_addition)
print("Sales data after subtraction:", sales_data_subtraction)
print("Sales data after multiplication:", sales_data_multiplication)
print("Sales data after division:", sales_data_division)
# -------------------------------------------------------------------------
# q3:Use Numpy to reshape the sales data into a different dimension
import numpy as np

# Load sales data from CSV file
sales_data = np.genfromtxt('sales.csv', delimiter=',', usecols=(3,))


reshaped_sales_data = np.reshape(sales_data, (1, 101))

# Print the reshaped sales data
print("Reshaped sales data:")
print(reshaped_sales_data)
# -----------------------------------------------------------------
# q4: Apply broadcasting to perform operations on arrays with different shapes
array1 = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
array2 = np.array([10, 20, 30])             # Shape: (3,)

# ...Perform broadcasting by adding the arrays
result = array1 + array2

#... Print the result
print("Result of broadcasting:")
print(result)
# --------------------------------------------------------------------
# q55: Use Numpy to perform matrix multiplication on sales data arrays
sales_data1 = np.array([[2, 3], [4, 5]])  # Example sales data array 1
sales_data2 = np.array([[1, 2], [3, 4]])  # Example sales data array 2

# Perform matrix multiplication
result = np.dot(sales_data1, sales_data2)
# you can also use @ operator

# Print the result
print("Result of matrix multiplication:")
print(result)