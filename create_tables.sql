CREATE TABLE sales (
        sales_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        customer_id INTEGER,
        sales_amount REAL,
        date DATE,
        region_id INTEGER,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (region_id) REFERENCES regions(region_id)
    );
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT,
        email TEXT,
        address TEXT
    );
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        product_category TEXT,
        product_description TEXT
    );
    CREATE TABLE regions (
        region_id INTEGER PRIMARY KEY,
        region_name TEXT
    )