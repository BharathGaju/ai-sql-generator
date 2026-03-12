import streamlit as st
import sqlite3
import pandas as pd
from groq import Groq
import os
from dotenv import load_dotenv

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
# ```

# ---

# ### Step 6: Create `.env` file
# ```
# GROQ_API_KEY=your-groq-api-key-here
# ```

# ### Step 7: Create `.gitignore`
# ```
# .env
# __pycache__/
# *.pyc
# sales.db
# ```

# ---

# ### Step 8: Run the app
# ```
# streamlit run app.py