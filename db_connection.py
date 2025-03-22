import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="localhost",     # Change if your MySQL runs on another host
    user="root",          # Replace with your MySQL username
    password="Mohan@123",  # Replace with your MySQL password
    database="ecommerce_db"  # Your database name
)

# Create a cursor object
cursor = conn.cursor()

# Test connection
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

# Close connection
cursor.close()
conn.close()
