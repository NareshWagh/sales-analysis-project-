"""
Sales Data Analysis Tool
------------------------
A short script to load our sales CSV file, calculate business metrics,
and plot our performance using Pandas and Matplotlib.

"""

import matplotlib.pyplot as plt
import pandas as pd

# ==========================================
# 1. Load and Clean the Data
# ==========================================

# Read the sales dataset from the local CSV file
df = pd.read_csv('Online Sales Data.csv')

# Clean up column names by stripping out any accidental leading/trailing spaces
df.columns = df.columns.str.strip()

# Convert the Date column from strings to actual datetime objects so we can work with dates
df["Date"] = pd.to_datetime(df["Date"], format="ISO8601")

# Create a new column grouping dates by Month (e.g., '2024-01') for our trend analysis
df["Month"] = df["Date"].dt.to_period("M")


# ==========================================
# 2. Run the Computations
# ==========================================

# Calculate overall total revenue by summing up the Total Revenue column
total_revenue = df["Total Revenue"].sum()

# Group sales by product name, sum their revenue, and sort them from highest to lowest
top_products = (
    df.groupby("Product Name")["Total Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Group total revenue by month to track sales trends over time
monthly_trends = df.groupby("Month")["Total Revenue"].sum()


# ==========================================
# 3. Print Results to Console
# ==========================================

print("==========================================")
print("          SALES PERFORMANCE REPORT        ")
print("==========================================")
print(f"Total Revenue Generated: ${total_revenue:,.2f}\n")
print("Top 3 Best Selling Products:")
print(top_products.head(3))
print("==========================================")


# ==========================================
# 4. Generate Visualizations
# ==========================================

# Top 10 products by revenue
top_10_products = top_products.head(10)

plt.figure(figsize=(10, 6))

top_10_products.plot(
    kind="bar",
    color="teal",
    edgecolor="black"
)

plt.title("Total Revenue by Product", fontsize=14, fontweight="bold")
plt.xlabel("Product Name", fontsize=11)
plt.ylabel("Revenue ($)", fontsize=11)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Monthly revenue trend

plt.figure(figsize=(10, 6))

monthly_trends.plot(
    kind="line",
    marker="o",
    color="darkorange",
    linewidth=2
)

plt.title("Monthly Revenue Trends", fontsize=14, fontweight="bold")
plt.xlabel("Month", fontsize=11)
plt.ylabel("Revenue ($)", fontsize=11)

# Add a grid to make the trend easier to read
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()
