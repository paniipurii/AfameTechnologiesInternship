import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  *** TASK 1: SALES DATA ANALYSIS *** 

# 1: Load the dataset
filepath = "C:\\Users\\asus\\Desktop\\ECOMMDATA.csv"
ecom_data = pd.read_csv(filepath)
print("Dataset preview:")
print(ecom_data.head())

# 2: Convert date columns to datetime format
ecom_data['Order Date'] = pd.to_datetime(ecom_data['Order Date'], errors='coerce')
ecom_data['Ship Date'] = pd.to_datetime(ecom_data['Ship Date'], errors='coerce')

# 3: Clean the dataset
# Dropping unnecessary columns
data_cleaned = ecom_data.drop(columns=['Row ID', 'Postal Code'], errors='ignore')

# Ensuring 'Sales' column is numeric
data_cleaned['Sales'] = pd.to_numeric(data_cleaned['Sales'], errors='coerce')

# 4: Calculate and display total sales
total_sales_value = data_cleaned['Sales'].sum()
print(f"Total Sales: ${total_sales_value:,.2f}")

# 5: Analyze sales trends over time
monthly_sales = data_cleaned.groupby(data_cleaned['Order Date'].dt.to_period('M')).sum(numeric_only=True)
plt.figure(figsize=(10, 6))
monthly_sales['Sales'].plot(kind='line', title="Monthly Sales Trend", xlabel="Month", ylabel="Total Sales ($)", color='blue')
plt.grid(alpha=0.5)
plt.savefig("monthly_sales_trend.png")
plt.show()

# 6: Identify best-selling products
best_selling_products = data_cleaned.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("Top 10 Best-Selling Products:")
print(best_selling_products)

# Visualization: Top 10 best-selling products
plt.figure(figsize=(10, 6))
best_selling_products.plot(kind='bar', title="Top 10 Best-Selling Products", xlabel="Product Name", ylabel="Total Sales ($)", color='green')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("top_10_products.png")
plt.show()

# 7: Visualize category-wise sales
category_wise_sales = data_cleaned.groupby('Category')['Sales'].sum()
print("Sales by Category:")
print(category_wise_sales)

plt.figure(figsize=(8, 8))
category_wise_sales.plot(kind='pie', autopct='%1.1f%%', title="Category-wise Sales Distribution", startangle=140, colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.ylabel('')  # Remove unnecessary ylabel
plt.tight_layout()
plt.savefig("category_sales_distribution.png")
plt.show()
