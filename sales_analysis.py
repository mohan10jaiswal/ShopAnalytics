import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Database connection using SQLAlchemy
db_url = "mysql+pymysql://root:Mohan%40123@localhost/ecommerce_db"
engine = create_engine(db_url)

# Load Orders data
query = "SELECT * FROM Orders;"
df_orders = pd.read_sql(query, engine)

# Convert all column names to lowercase to avoid case mismatch errors
df_orders.columns = df_orders.columns.str.lower()

# Convert order_date column to datetime (case-insensitive handling)
if 'order_date' in df_orders.columns:
    df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
else:
    print(" Column 'order_date' not found! Check column names above.")


#OVERVIEW OF DATA Mohan Bhai 

print(df_orders.head())
# Summary statistics
print(df_orders.describe())
# Count of unique customers
print("\nUnique Customers:", df_orders['customer_id'].nunique())
# Count of unique products sold
print("\nUnique Products Sold:", df_orders['product_id'].nunique())
# Total revenue
total_revenue = df_orders['total_amount'].sum()
print("\nTotal Revenue: ₹", total_revenue)


#monthly revenue trends
# Extracting Month-Year for trend analysis
df_orders['order_month'] = df_orders['order_date'].dt.to_period('M')

# Grouping by month to get total revenue per month
monthly_sales = df_orders.groupby('order_month')['total_amount'].sum().reset_index()

# Convert period to string for plotting
monthly_sales['order_month'] = monthly_sales['order_month'].astype(str)

# Plot
plt.figure(figsize=(12,5))
sns.lineplot(x='order_month', y='total_amount', data=monthly_sales, marker='o', color='b')

plt.title('Monthly Sales Trend', fontsize=14)
plt.xlabel('Month-Year')
plt.ylabel('Total Sales (₹)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


#Top-Selling Products
# Top-selling products
top_products = df_orders.groupby('product_id')['total_amount'].sum().reset_index()
top_products = top_products.sort_values(by='total_amount', ascending=False).head(10)

# Plot
plt.figure(figsize=(12,5))
sns.barplot(x='product_id', y='total_amount', data=top_products, palette='viridis')

plt.title('Top-Selling Products', fontsize=14)
plt.xlabel('Product ID')
plt.ylabel('Total Sales (₹)')
plt.xticks(rotation=45)
plt.show()


# Top Customers by Spending
# Top spending customers
top_customers = df_orders.groupby('customer_id')['total_amount'].sum().reset_index()
top_customers = top_customers.sort_values(by='total_amount', ascending=False).head(10)

# Plot
plt.figure(figsize=(12,5))
sns.barplot(x='customer_id', y='total_amount', data=top_customers, palette='magma')

plt.title('Top 10 Customers by Spending', fontsize=14)
plt.xlabel('Customer ID')
plt.ylabel('Total Spend (₹)')
plt.xticks(rotation=45)
plt.show()



# Get the top 3 customers based on total revenue
top_3_customers = top_customers.head(3)  # Ensure this exists

# Modify labels to show "Customer ID: X"
labels = [f"Customer {cid}" for cid in top_3_customers['customer_id']]

# Plot Pie Chart with better labels
plt.figure(figsize=(8, 8))
plt.pie(top_3_customers['total_amount'], labels=labels, autopct='%1.1f%%', 
        colors=sns.color_palette("viridis", len(top_3_customers)))

plt.title(" Top 3 Customers' Contribution to Revenue")
plt.show()







