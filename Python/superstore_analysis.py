# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("superstore_clean_data.csv", encoding="latin1")

# First 5 Rows
print("First 5 rows:")
print(df.head())

# Dataset Size
print("\nDataset size:")
print(df.shape)

# Columns
print("\nColumns:")
print(df.columns)

# KPIs
print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Total Quantity:", df["Quantity"].sum())

# Sales by Region
sales_by_region = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(sales_by_region)

sales_by_region.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()

# Profit by Category
profit_by_category = df.groupby("Category")["Profit"].sum()

print("\nProfit by Category:")
print(profit_by_category)

profit_by_category.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.show()

# Sales by Sub-Category
sales_by_subcategory = df.groupby("Sub-Category")["Sales"].sum()

print("\nSales by Sub-Category:")
print(sales_by_subcategory)

sales_by_subcategory.plot(kind="bar")

plt.title("Sales by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")

plt.show()