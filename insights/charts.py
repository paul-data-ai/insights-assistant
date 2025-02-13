import matplotlib.pyplot as plt
import seaborn as sns
import io

# Function to generate a bar chart for sales by payment method
def plot_sales_by_payment(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(x="payment_method", y="total_sales", data=df)
    plt.xlabel("Payment Method")
    plt.ylabel("Total Sales")
    plt.title("Sales by Payment Method")
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Function to generate a bar chart for top-selling products
def plot_top_selling_products(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(x="total_sold", y="product_name", data=df.sort_values("total_sold", ascending=False))
    plt.xlabel("Total Sold")
    plt.ylabel("Product Name")
    plt.title("Top Selling Products")
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Function to generate a pie chart for sales performance by region
def plot_sales_performance_by_region(df):
    plt.figure(figsize=(7, 7))
    plt.pie(df["total_sales"], labels=df["region"], autopct="%1.1f%%", startangle=140)
    plt.title("Sales Performance by Region")
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Function to generate a pie chart for customer type analysis
def plot_customer_type_analysis(df):
    plt.figure(figsize=(7, 7))
    plt.pie(df["customer_count"], labels=df["customer_type"], autopct="%1.1f%%", startangle=140)
    plt.title("Customer Type Distribution")
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Function to generate a bar chart for sales channel comparison
def plot_sales_channel_comparison(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(x="sales_channel", y="total_sales", data=df)
    plt.xlabel("Sales Channel")
    plt.ylabel("Total Sales")
    plt.title("Sales Channel Comparison")
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Function to generate a boxplot for average sale price
def plot_average_sale_price(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="sale_type", y="average_price", data=df)
    plt.xlabel("Sale Type")
    plt.ylabel("Average Sale Price")
    plt.title("Average Sale Price by Sale Type")
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Function to generate a line chart for sales trend over time
def plot_sales_trend_over_time(df):
    plt.figure(figsize=(10, 5))
    sns.lineplot(x="sale_date", y="total_sales", data=df)
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.title("Sales Trend Over Time")
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Function to generate a bar chart for sales performance by salesperson
def plot_sales_performance_by_salesperson(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(x="total_sales", y="salesperson_name", data=df.sort_values("total_sales", ascending=False))
    plt.xlabel("Total Sales")
    plt.ylabel("Salesperson")
    plt.title("Sales Performance by Salesperson")
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Function to generate a pie chart for refund status analysis
def plot_refund_status_analysis(df):
    plt.figure(figsize=(7, 7))
    plt.pie(df["refund_count"], labels=df["refund_status"], autopct="%1.1f%%", startangle=140)
    plt.title("Refund Status Distribution")
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Function to generate a bar chart for highest-value sales
def plot_highest_value_sales(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(x="order_id", y="total_value", data=df.sort_values("total_value", ascending=False).head(10))
    plt.xlabel("Order ID")
    plt.ylabel("Total Sale Value")
    plt.title("Highest Value Sales")
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf
