import streamlit as st
import sqlite3
import pandas as pd
from groq import Groq
import os
from dotenv import load_dotenv

def create_database():
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY, name TEXT, city TEXT, age INTEGER, email TEXT)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY, product_name TEXT, category TEXT, price REAL)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER,
        quantity INTEGER, order_date TEXT, total_amount REAL)""")

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

# Create database when app starts
create_database()

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Database schema info for AI
SCHEMA = """
Tables in the database:

1. customers (customer_id, name, city, age, email)
2. products (product_id, product_name, category, price)
3. orders (order_id, customer_id, product_id, quantity, order_date, total_amount)
"""

def generate_sql(question):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": f"""You are a SQL expert. 
            Convert natural language questions to SQLite SQL queries.
            Only return the SQL query, nothing else. No explanations, no markdown, just the raw SQL.
            
            Database schema:
            {SCHEMA}"""},
            {"role": "user", "content": f"Convert this to SQL: {question}"}
        ]
    )
    return response.choices[0].message.content.strip()

def run_sql(query):
    conn = sqlite3.connect("sales.db")
    try:
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df, None
    except Exception as e:
        conn.close()
        return None, str(e)

# Page title
st.title("🗄️ Natural Language to SQL Generator")
st.write("Ask questions about your data in plain English!")

# Show database schema
with st.expander("📋 View Database Schema"):
    st.code(SCHEMA)

# Sample questions
st.subheader("💡 Try these questions:")
col1, col2 = st.columns(2)
with col1:
    st.info("Show me all customers from Mumbai")
    st.info("What are the top 5 most expensive products?")
    st.info("How many orders were placed in January 2024?")
with col2:
    st.info("Which customer spent the most money?")
    st.info("Show total sales by product category")
    st.info("List all electronics products")

st.divider()

# Question input
question = st.text_input("🤔 Ask your question:", 
                          placeholder="e.g. Show me all customers from Mumbai")

if question:
    with st.spinner("🤖 AI is generating SQL..."):
        # Generate SQL
        sql_query = generate_sql(question)

        # Show generated SQL
        st.subheader("⚡ Generated SQL Query:")
        st.code(sql_query, language="sql")

        # Run the query
        df, error = run_sql(sql_query)

        if error:
            st.error(f"❌ Error running query: {error}")
        else:
            st.subheader("📊 Results:")
            st.dataframe(df)
            st.success(f"✅ Found {len(df)} records!")
