Sales Data Analysis
A Python data analysis project that explores online sales data using Pandas and Matplotlib.

Project Overview
This project analyzes an online sales dataset to answer key business questions:

What is the total revenue generated?
Which products generate the most revenue?
How does revenue change over time?
What are the top-performing products?
The analysis includes data cleaning, aggregation, reporting, and visualization.

Features
Load sales data from a CSV file
Clean column names
Convert dates into datetime format
Calculate total revenue
Identify top-selling products
Analyze monthly revenue trends
Generate revenue visualizations using Matplotlib
Technologies Used

Python
Pandas
Matplotlib

Project Structure
sales-data-analysis/
│
├── sales_analysis.py
├── Online Sales Data.csv
├── requirements.txt
├── README.md
└── images/
    ├── revenue_by_product.png
    └── monthly_trends.png
Installation
Clone the repository:



cd sales-data-analysis
Install dependencies:

pip install -r requirements.txt
Running the Project
python sales_analysis.py
Sample Output
==========================================
          SALES PERFORMANCE REPORT
==========================================
Total Revenue Generated: $1,234,567.89

Top 3 Best Selling Products:
Laptop        250000
Smartphone    210000
Tablet        180000
==========================================
Visualizations
Top 10 Products by Revenue
Displays the highest revenue-generating products.

Monthly Revenue Trends
Shows revenue performance over time.

Learning Objectives
This project demonstrates:

Data cleaning with Pandas
Data aggregation using GroupBy
Datetime handling
Business KPI reporting
Data visualization using Matplotlib
