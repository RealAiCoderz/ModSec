--q1 SQL query to retrieve total sales amount for each product category.

SELECT products.category, SUM(sales.sales_amount) AS total_sales
FROM sales
JOIN products ON sales.product_id = products.product_id
GROUP BY products.category;

--q2 join operation to retrieve sales data along with product information.

SELECT sales.sales_id, sales.sales_amount, sales.date, products.product_id, products.product_name, products.category
FROM sales
JOIN products ON sales.product_id = products.product_id limit 5;

--q3 subquery to find customers who made the highest purchase.

SELECT customers.customer_id, customers.customer_name, customers.email, customers.address
FROM customers
WHERE customers.customer_id IN (
    SELECT sales.customer_id
    FROM sales
    GROUP BY sales.customer_id
    ORDER BY SUM(sales.sales_amount) DESC
    LIMIT 1
);

--q4 GROUP BY clause to calculate the average sales amount by month and year.

SELECT 
    strftime('%Y', date) AS year, 
    strftime('%m', date) AS month, 
    AVG(sales_amount) AS average_sales
FROM sales
GROUP BY year, month;

--q5 SQL query to find the top-selling products by region.
SELECT regions.region_name, products.product_name, COUNT(sales.sales_amount) AS total_sales
FROM sales
JOIN products ON sales.product_id = products.product_id
JOIN regions ON sales.region_id = regions.region_id
GROUP BY regions.region_name, products.product_name
ORDER BY total_sales DESC;