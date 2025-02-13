import os
import pandas as pd
from datetime import datetime
import requests

from database.conn import get_engine

from insights.queries import (  # Import the queries
    get_total_sales_by_payment_method,
    get_top_selling_products,
    get_sales_performance_by_region,
    get_customer_type_analysis,
    get_sales_channel_comparison,
    get_average_sale_price,
    get_sales_trend_over_time,
    get_sales_performance_by_salesperson,
    get_refund_status_analysis,
    get_highest_value_sales
)



# Function to fetch and display insights
def fetch_insights():
    insights = f"📊 *Auto-Generated Data Insights* 📊\n📅 {datetime.now().strftime('%Y-%m-%d %H:%M')} \n\n"
    
    # Create a dictionary for each query and its title
    query_titles = {
        "Total Sales by Payment Method": get_total_sales_by_payment_method(),
        "Top Selling Products": get_top_selling_products(),
        "Sales Performance by Region": get_sales_performance_by_region(),
        "Customer Type Analysis": get_customer_type_analysis(),
        "Sales Channel Comparison": get_sales_channel_comparison(),
        "Average Sale Price": get_average_sale_price(),
        "Sales Trend Over Time (Daily)": get_sales_trend_over_time(),
        "Sales Performance by Salesperson": get_sales_performance_by_salesperson(),
        "Refund Status Analysis": get_refund_status_analysis(),
        "Highest Value Sales": get_highest_value_sales()
    }
    
    # Process each query and collect the insights with proper titles
    for title, query in query_titles.items():
        df = pd.read_sql(query, conn)
        if not df.empty:
            insights += f"*{title}*:\n"  # Add the title for each insight
            insights += f"```\n{df.to_string(index=False)}\n```\n\n"  # Display the result in a readable format
        return insights

# Send insights to Slack
def send_to_slack(insights):
    SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK')
    if SLACK_WEBHOOK_URL:
        try:
            response = requests.post(SLACK_WEBHOOK_URL, json={"text": insights})
            response.raise_for_status()  # Raises error for bad responses (4xx, 5xx)
            print("Message sent to Slack!")
        except requests.exceptions.RequestException as e:
            print(f"Error sending message to Slack: {e}")
    else:
        print("SLACK_WEBHOOK_URL is not set properly.")

# Main function
if __name__ == "__main__":
    insights = fetch_insights()
    send_to_slack(insights)

# Close DB connection
conn.close()


