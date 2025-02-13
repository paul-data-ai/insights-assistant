import matplotlib.pyplot as plt
import seaborn as sns
import io

# Set Seaborn theme for consistent styling
sns.set_theme(style="whitegrid")

# Function to generate a bar chart for sales by payment method
def plot_sales_by_payment(df):
    df = df.dropna(subset=["payment_method", "total_sales"])  # Handle missing data
    plt.figure(figsize=(8, 5))
    sns.barplot(x="payment_method", y="total_sales", data=df)
    plt.xlabel("Payment Method")
    plt.ylabel("Total Sales")
    plt.title("Sales by Payment Method")
    plt.xticks(rotation=45)  # Rotate labels for better readability

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")  # Avoid label cut-off
    buf.seek(0)
    return buf

# Function to generate a bar chart for top-selling products
def plot_top_selling_products(df):
    df = df.dropna(subset=["product_name", "total_quantity_sold"])
    plt.figure(figsize=(8, 5))
    sns.barplot(
        x="total_quantity_sold",
        y="product_name",
        data=df.sort_values("total_quantity_sold", ascending=False),
    )
    plt.xlabel("Total Sold")
    plt.ylabel("Product Name")
    plt.title("Top Selling Products")

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return buf

# Function to generate a pie chart for sales performance by region
def plot_sales_performance_by_region(df):
    df = df.dropna(subset=["region", "total_revenue"])
    plt.figure(figsize=(7, 7))
    plt.pie(df["total_revenue"], labels=df["region"].astype(str), autopct="%1.1f%%", startangle=140)
    plt.title("Sales Performance by Region")
    plt.gca().set_aspect("equal")  # Ensure pie is circular

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return buf

# Function to generate a pie chart for customer type analysis
def plot_customer_type_analysis(df):
    df = df.dropna(subset=["customer_type", "customer_count"])
    plt.figure(figsize=(7, 7))
    plt.pie(df["customer_count"], labels=df["customer_type"].astype(str), autopct="%1.1f%%", startangle=140)
    plt.title("Customer Type Distribution")
    plt.gca().set_aspect("equal")

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return buf

# Function to generate a bar chart for sales channel comparison
def plot_sales_channel_comparison(df):
    df = df.dropna(subset=["sales_channel", "total_revenue"])
    plt.figure(figsize=(8, 5))
    sns.barplot(x="sales_channel", y="total_revenue", data=df)
    plt.xlabel("Sales Channel")
    plt.ylabel("Total Revenue")
    plt.title("Sales Channel Comparison")
    plt.xticks(rotation=45)

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return buf

# Function to generate a line chart for sales trend over time
def plot_sales_trend_over_time(df):
    df = df.dropna(subset=["sale_date", "total_revenue"])
    plt.figure(figsize=(10, 5))
    sns.lineplot(x="sale_date", y="total_revenue", data=df, marker="o")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.title("Sales Trend Over Time")
    plt.xticks(rotation=45)

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return buf

# Function to generate a bar chart for sales performance by salesperson
def plot_sales_performance_by_salesperson(df):
    df = df.dropna(subset=["salesperson_name", "total_revenue"])
    plt.figure(figsize=(8, 5))
    sns.barplot(
        x="total_revenue",
        y="salesperson_name",
        data=df.sort_values("total_revenue", ascending=False),
    )
    plt.xlabel("Total Sales")
    plt.ylabel("Salesperson")
    plt.title("Sales Performance by Salesperson")

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return buf
