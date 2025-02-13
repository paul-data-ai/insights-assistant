import matplotlib.pyplot as plt
import seaborn as sns
import io

def generate_chart(func, df):
    """ Generic function to generate a chart and return it as a BytesIO object."""
    if df.empty:
        print("Warning: Empty DataFrame received, skipping chart.")
        return None
    
    buf = io.BytesIO()
    func(df)  # Call the specific chart function
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close()  # Prevent memory leaks
    buf.seek(0)
    return buf

# Function to generate a bar chart for sales by payment method
def plot_sales_by_payment(df):
    required_columns = {"payment_method", "total_sales"}
    if not required_columns.issubset(df.columns):
        print("Missing required columns for plot_sales_by_payment")
        return None
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x="payment_method", y="total_sales", data=df)
    plt.xlabel("Payment Method")
    plt.ylabel("Total Sales")
    plt.title("Sales by Payment Method")
    
    return generate_chart(plt.show, df)

# Function to generate a bar chart for top-selling products
def plot_top_selling_products(df):
    required_columns = {"product_name", "total_quantity_sold"}
    if not required_columns.issubset(df.columns):
        print("Missing required columns for plot_top_selling_products")
        return None
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x="total_quantity_sold", y="product_name", data=df.sort_values("total_sold", ascending=False))
    plt.xlabel("Total Sold")
    plt.ylabel("Product Name")
    plt.title("Top Selling Products")
    
    return generate_chart(plt.show, df)

# Function to generate a pie chart for sales performance by region
def plot_sales_performance_by_region(df):
    required_columns = {"region", "total_revenue"}
    if not required_columns.issubset(df.columns):
        print("Missing required columns for plot_sales_performance_by_region")
        return None
    
    plt.figure(figsize=(7, 7))
    plt.pie(df["total_revenue"], labels=df["region"], autopct="%1.1f%%", startangle=140)
    plt.title("Sales Performance by Region")
    
    return generate_chart(plt.show, df)

# Function to generate a pie chart for customer type analysis
def plot_customer_type_analysis(df):
    required_columns = {"customer_type", "customer_count"}
    if not required_columns.issubset(df.columns):
        print("Missing required columns for plot_customer_type_analysis")
        return None
    
    plt.figure(figsize=(7, 7))
    plt.pie(df["customer_count"], labels=df["customer_type"], autopct="%1.1f%%", startangle=140)
    plt.title("Customer Type Distribution")
    
    return generate_chart(plt.show, df)

# Function to generate a bar chart for sales channel comparison
def plot_sales_channel_comparison(df):
    required_columns = {"sales_channel", "total_revenue"}
    if not required_columns.issubset(df.columns):
        print("Missing required columns for plot_sales_channel_comparison")
        return None
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x="sales_channel", y="total_revenue", data=df)
    plt.xlabel("Sales Channel")
    plt.ylabel("Total Revenue")
    plt.title("Sales Channel Comparison")
    
    return generate_chart(plt.show, df)

# Function to generate a line chart for sales trend over time
def plot_sales_trend_over_time(df):
    required_columns = {"sale_date", "total_revenue"}
    if not required_columns.issubset(df.columns):
        print("Missing required columns for plot_sales_trend_over_time")
        return None
    
    plt.figure(figsize=(10, 5))
    sns.lineplot(x="sale_date", y="total_revenue", data=df)
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.title("Sales Trend Over Time")
    
    return generate_chart(plt.show, df)

# Function to generate a bar chart for sales performance by salesperson
def plot_sales_performance_by_salesperson(df):
    required_columns = {"salesperson_name", "total_revenue"}
    if not required_columns.issubset(df.columns):
        print("Missing required columns for plot_sales_performance_by_salesperson")
        return None
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x="total_revenue", y="salesperson_name", data=df.sort_values("total_revenue", ascending=False))
    plt.xlabel("Total Sales")
    plt.ylabel("Salesperson")
    plt.title("Sales Performance by Salesperson")
    
    return generate_chart(plt.show, df)
