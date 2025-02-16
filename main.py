import pandas as pd
from datetime import datetime
import requests
import os
from io import BytesIO
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from database.conn import get_engine
from insights.queries import (  # Import the queries
    get_total_sales_by_payment_method,
    get_top_selling_products,
    get_sales_performance_by_region,
    get_customer_type_analysis,
    get_sales_channel_comparison,
    # get_average_sale_price,
    get_sales_trend_over_time,
    get_sales_performance_by_salesperson,
    # get_refund_status_analysis,
    # get_highest_value_sales
)

from insights.charts import (  # Import all chart functions
    plot_sales_by_payment,
    plot_top_selling_products,
    plot_sales_performance_by_region,
    plot_customer_type_analysis,
    plot_sales_channel_comparison,
    # plot_average_sale_price,
    plot_sales_trend_over_time,
    plot_sales_performance_by_salesperson,
    # plot_refund_status_analysis,
    # plot_highest_value_sales
)

from llm.llm import generate_actionables

# Get database connection
conn = get_engine().connect()

# Function to fetch and display insights
def format_number(value):
    """Formats numbers with commas and two decimal places if they are floats/integers."""
    if isinstance(value, (int, float)):
        return f"{value:,.2f}"  # Adds commas and keeps two decimal places
    return value  # Return as is if it's not a number

def format_dataframe(df):
    """Applies formatting to all numerical values in a DataFrame."""
    return df.map(format_number)  # Replaces applymap with map


def fetch_insights():
    insights = f"📊 *Auto-Generated Data Insights* 📊\n📅 {datetime.now().strftime('%Y-%m-%d %H:%M')} \n\n"
    images = []
    dataframes = {}

    query_titles = {
        "Total Sales by Payment Method": (get_total_sales_by_payment_method(), plot_sales_by_payment),
        "Top Selling Products": (get_top_selling_products(), plot_top_selling_products),
        "Sales Performance by Region": (get_sales_performance_by_region(), plot_sales_performance_by_region),
        "Customer Type Analysis": (get_customer_type_analysis(), plot_customer_type_analysis),
        "Sales Channel Comparison": (get_sales_channel_comparison(), plot_sales_channel_comparison),
        "Sales Trend Over Time (Daily)": (get_sales_trend_over_time(), plot_sales_trend_over_time),
        "Sales Performance by Salesperson": (get_sales_performance_by_salesperson(), plot_sales_performance_by_salesperson),
    }

    for title, (query, chart_function) in query_titles.items():
        df = pd.read_sql(query, conn)
        if not df.empty:
            formatted_df = format_dataframe(df)
            insights += f"*{title}*:\n"
            insights += f"```\n{formatted_df.to_string(index=False)}\n```\n\n"
            images.append(chart_function(df))
            dataframes[title] = df  # Store DataFrame for CSV upload

    return insights, images, dataframes

# Load environment variables
SLACK_CHANNEL = "#insights"  
client = WebClient(token=os.getenv('SLACK_BOT_TOKEN'))


# Send insights, images, and CSV files to Slack
def send_to_slack(insights):
    """Sends text-based insights to Slack."""
    try:
        client.chat_postMessage(channel=SLACK_CHANNEL, text=insights)
        print("✅ Insights sent to Slack!")
    except SlackApiError as e:
        print(f"⚠️ Error sending message to Slack: {e.response['error']}")

# Main function
if __name__ == "__main__":
    insights, images, dataframes = fetch_insights()
    send_to_slack(generate_actionables(insights))
    conn.close()