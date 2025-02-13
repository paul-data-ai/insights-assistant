import pandas as pd
from datetime import datetime
import requests
import os

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

from insights.charts import (  # Import all chart functions
    plot_sales_by_payment,
    plot_top_selling_products,
    plot_sales_performance_by_region,
    plot_customer_type_analysis,
    plot_sales_channel_comparison,
    plot_average_sale_price,
    plot_sales_trend_over_time,
    plot_sales_performance_by_salesperson,
    plot_refund_status_analysis,
    plot_highest_value_sales
)


# Get database connection
conn = get_engine().connect()

# Function to fetch and display insights
def fetch_insights():
    insights = f"📊 *Auto-Generated Data Insights* 📊\n📅 {datetime.now().strftime('%Y-%m-%d %H:%M')} \n\n"
    images = []

    query_titles = {
        "Total Sales by Payment Method": (get_total_sales_by_payment_method(), plot_sales_by_payment),
        "Top Selling Products": (get_top_selling_products(), plot_top_selling_products),
        "Sales Performance by Region": (get_sales_performance_by_region(), plot_sales_performance_by_region),
        "Customer Type Analysis": (get_customer_type_analysis(), plot_customer_type_analysis),
        "Sales Channel Comparison": (get_sales_channel_comparison(), plot_sales_channel_comparison),
        "Average Sale Price": (get_average_sale_price(), plot_average_sale_price),
        "Sales Trend Over Time (Daily)": (get_sales_trend_over_time(), plot_sales_trend_over_time),
        "Sales Performance by Salesperson": (get_sales_performance_by_salesperson(), plot_sales_performance_by_salesperson),
        "Refund Status Analysis": (get_refund_status_analysis(), plot_refund_status_analysis),
        "Highest Value Sales": (get_highest_value_sales(), plot_highest_value_sales)
    }

    for title, (query, chart_function) in query_titles.items():
        df = pd.read_sql(query, conn)
        if not df.empty:
            insights += f"*{title}*:\n"
            insights += f"```\n{df.to_string(index=False)}\n```\n\n"
            images.append(chart_function(df))  # ✅ Generate and store the chart
    
    return insights, images  # ✅ Return insights & images

# Function to send insights and images to Slack
def send_to_slack(insights, images):
    SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK')
    
    if SLACK_WEBHOOK_URL:
        try:
            # Send text insights
            response = requests.post(SLACK_WEBHOOK_URL, json={"text": insights})
            response.raise_for_status()
            
            # Send charts as images
            for i, img in enumerate(images):
                requests.post(
                    SLACK_WEBHOOK_URL,
                    files={"file": (f"chart_{i}.png", img, "image/png")},
                    data={"channels": "#insights"}
                )

            print("Message & charts sent to Slack!")

        except requests.exceptions.RequestException as e:
            print(f"Error sending message to Slack: {e}")

    else:
        print("SLACK_WEBHOOK_URL is not set properly.")

# Main function
if __name__ == "__main__":
    insights, images = fetch_insights()
    send_to_slack(insights, images)
    
    # Close the database connection
    conn.close()