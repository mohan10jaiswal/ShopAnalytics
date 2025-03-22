import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mohan@123",
    database="ecommerce_db"
)

# Load data into Pandas
query = "SELECT * FROM Customers;"
df = pd.read_sql(query, conn)

# Display data
print(df.head())

# Close connection
conn.close()
