# queries.py

# 1. Total Sales by Payment Method
def get_total_sales_by_payment_method():
    return """
    SELECT 
        payment_method,
        COUNT(*) AS total_sales,
        SUM(price * quantity) AS total_revenue
    FROM sales
    GROUP BY payment_method
    ORDER BY total_revenue DESC;
    """

# 2. Top Selling Products
def get_top_selling_products():
    return """
    SELECT 
        product_name,
        SUM(quantity) AS total_quantity_sold,
        SUM(price * quantity) AS total_revenue
    FROM sales
    GROUP BY product_name
    ORDER BY total_quantity_sold DESC
    LIMIT 10;
    """

# 3. Sales Performance by Region
def get_sales_performance_by_region():
    return """
    SELECT 
        region,
        COUNT(*) AS total_sales,
        SUM(price * quantity) AS total_revenue
    FROM sales
    GROUP BY region
    ORDER BY total_revenue DESC
    LIMIT 10;
    """

# 4. Customer Type Analysis
def get_customer_type_analysis():
    return """
    SELECT 
        customer_type,
        COUNT(*) AS customer_count
    FROM sales
    GROUP BY customer_type
    ORDER BY customer_count DESC;
    """

# 5. Sales Channel Comparison
def get_sales_channel_comparison():
    return """
    SELECT 
        sales_channel,
        SUM(price * quantity) AS total_revenue
    FROM sales
    GROUP BY sales_channel
    ORDER BY total_revenue DESC;
    """


# 7. Sales Trend Over Time (Daily)
def get_sales_trend_over_time():
    return """
    SELECT 
        DATE(sold_at) AS sale_date,
        SUM(price * quantity) AS total_revenue
    FROM sales
    GROUP BY sale_date
    ORDER BY sale_date DESC
    LIMIT 10;
    """

# 8. Sales Performance by Salesperson
def get_sales_performance_by_salesperson():
    return """
    SELECT 
        salesperson_name,
        SUM(price * quantity) AS total_revenue
    FROM sales
    GROUP BY salesperson_name
    ORDER BY total_revenue DESC;
    """
