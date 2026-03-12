import sqlite3
import pandas as pd

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Create customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT,
    age INTEGER,
    email TEXT
)
""")

# Create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL
)
""")

# Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TEXT,
    total_amount REAL
)
""")

# Insert sample customers
customers = [
    (1, "Rahul Sharma", "Mumbai", 28, "rahul@email.com"),
    (2, "Priya Singh", "Delhi", 32, "priya@email.com"),
    (3, "Amit Patel", "Bangalore", 25, "amit@email.com"),
    (4, "Sneha Reddy", "Hyderabad", 29, "sneha@email.com"),
    (5, "Vikram Kumar", "Chennai", 35, "vikram@email.com"),
    (6, "Neha Gupta", "Pune", 27, "neha@email.com"),
    (7, "Rajesh Verma", "Kolkata", 31, "rajesh@email.com"),
    (8, "Ananya Joshi", "Mumbai", 26, "ananya@email.com"),
]

# Insert sample products
products = [
    (1, "Laptop", "Electronics", 55000),
    (2, "Smartphone", "Electronics", 25000),
    (3, "Headphones", "Electronics", 3000),
    (4, "Desk Chair", "Furniture", 8000),
    (5, "Coffee Maker", "Appliances", 4500),
    (6, "Running Shoes", "Sports", 3500),
    (7, "Backpack", "Accessories", 2000),
    (8, "Monitor", "Electronics", 18000),
]

# Insert sample orders
orders = [
    (1, 1, 1, 1, "2024-01-15", 55000),
    (2, 2, 2, 2, "2024-01-20", 50000),
    (3, 3, 3, 1, "2024-02-01", 3000),
    (4, 4, 4, 2, "2024-02-10", 16000),
    (5, 5, 5, 1, "2024-02-15", 4500),
    (6, 1, 6, 1, "2024-03-01", 3500),
    (7, 2, 7, 3, "2024-03-10", 6000),
    (8, 3, 8, 1, "2024-03-15", 18000),
    (9, 6, 1, 1, "2024-03-20", 55000),
    (10, 7, 2, 1, "2024-04-01", 25000),
    (11, 8, 3, 2, "2024-04-05", 6000),
    (12, 4, 6, 1, "2024-04-10", 3500),
]

cursor.executemany("INSERT OR IGNORE INTO customers VALUES (?,?,?,?,?)", customers)
cursor.executemany("INSERT OR IGNORE INTO products VALUES (?,?,?,?)", products)
cursor.executemany("INSERT OR IGNORE INTO orders VALUES (?,?,?,?,?,?)", orders)

conn.commit()
conn.close()

print("✅ Database created successfully!")
print("Tables: customers, products, orders")
print("Sample data inserted!")
 

# ### Step 4: Run it to create the database
# ```
# python create_database.py