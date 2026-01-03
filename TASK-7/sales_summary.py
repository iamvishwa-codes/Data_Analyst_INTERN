import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# STEP 1: Create & Connect DB
# ---------------------------
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

sales_data = [
    ("Laptop", 5, 60000),
    ("Laptop", 3, 60000),
    ("Phone", 10, 20000),
    ("Phone", 5, 20000),
    ("Headphones", 15, 1500),
    ("Headphones", 10, 1500)
]

cursor.executemany(
    "INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)",
    sales_data
)

conn.commit()

# ---------------------------
# STEP 2: SQL Query
# ---------------------------
query = """
SELECT 
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)

print("\n📊 SALES SUMMARY")
print(df)

conn.close()

# ---------------------------
# STEP 3: Visualization
# ---------------------------
df.plot(kind='bar', x='product', y='revenue')

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig("sales_chart.png")
plt.show()
