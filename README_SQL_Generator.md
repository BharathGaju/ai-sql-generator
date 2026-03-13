# 🗄️ Natural Language to SQL Generator

An intelligent web application that converts plain English business questions into executable SQL queries using LLM APIs — making data accessible to everyone, no SQL knowledge required.

---

## 🌐 Live Demo
👉 [Open Live App](https://bharathgaju-ai-sql-generator.streamlit.app)

---

## 📌 Overview

Writing SQL queries is a barrier for many business users who want to explore data. This app bridges that gap — type any business question in plain English and instantly get the SQL query generated, executed, and results displayed. Powered by LLaMA 3.3 via Groq API.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 💬 Natural Language Input | Type questions in plain English |
| ⚡ Auto SQL Generation | AI converts question to SQL instantly |
| ▶️ Query Execution | Runs generated SQL on live database |
| 📊 Results Display | Shows query results in a clean table |
| 📋 Schema Viewer | View database structure at any time |
| 💡 Sample Questions | Pre-built example questions to get started |
| ✅ Record Count | Shows how many records were returned |

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit** — Web application framework
- **Groq API (LLaMA 3.3)** — Natural language to SQL conversion
- **SQLite** — Lightweight database
- **Pandas** — Query result handling and display
- **python-dotenv** — Environment variable management

---

## 🗃️ Database Schema

The app comes with a pre-built sample e-commerce database:

```
customers   → customer_id, name, city, age, email
products    → product_id, product_name, category, price
orders      → order_id, customer_id, product_id, quantity, order_date, total_amount
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/BharathGaju/ai-sql-generator.git
cd ai-sql-generator
```

### 2. Install dependencies
```bash
pip install streamlit groq python-dotenv pandas
```

### 3. Set up API key
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your-groq-api-key-here
```
Get your free API key at: https://console.groq.com/

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📂 Project Structure

```
ai-sql-generator/
│
├── app.py                  # Main Streamlit application
├── create_database.py      # Script to create sample database
├── requirements.txt        # Python dependencies
├── .env                    # API key (not committed to GitHub)
├── .gitignore              # Git ignore file
└── README.md               # Project documentation
```

---

## 💡 How It Works

```
User types question in plain English
      ↓
Question + database schema sent to Groq LLM
      ↓
LLM generates appropriate SQL query
      ↓
App executes SQL on SQLite database
      ↓
Results displayed in interactive table
```

---

## 📝 Example Queries

| Natural Language | Generated SQL |
|-----------------|---------------|
| Show me all customers from Mumbai | `SELECT * FROM customers WHERE city = 'Mumbai'` |
| Which customer spent the most money? | `SELECT customer_id, SUM(total_amount) FROM orders GROUP BY customer_id ORDER BY SUM(total_amount) DESC LIMIT 1` |
| Show total sales by product category | `SELECT p.category, SUM(o.total_amount) FROM orders o JOIN products p ON o.product_id = p.product_id GROUP BY p.category` |
| Top 5 most expensive products | `SELECT * FROM products ORDER BY price DESC LIMIT 5` |

---

## 🎯 Use Cases

- **Business Analysts** — Query databases without SQL knowledge
- **Managers** — Get instant answers from data
- **Data Teams** — Prototype queries faster
- **E-Commerce** — Analyze sales, customers, and products easily
- **Students** — Learn SQL by seeing natural language converted to queries

---

## 📦 Requirements

```
streamlit
groq
python-dotenv
pandas
```

---

## 👨‍💻 Author

**Bharath KG** — Data Analyst  
📧 bharath4637@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/bharath-k-g-2971a5bb)  
🐙 [GitHub](https://github.com/BharathGaju)

---

## ⭐ If you found this useful, please give it a star!
