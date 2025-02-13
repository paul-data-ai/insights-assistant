import os
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import requests

# Set up database connection using SQLAlchemy
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')

# Construct the database URL for SQLAlchemy
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Get all tables in the public schema
query = "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';"
tables = pd.read_sql(query, engine)

insights = f"📊 *Auto-Generated Data Insights* 📊\n📅 {datetime.now().strftime('%Y-%m-%d %H:%M')} \n\n"

# Analyze each table
for table in tables["tablename"]:
    data_query = f"SELECT * FROM {table} LIMIT 1000"
    df = pd.read_sql(data_query, engine)

    if df.empty:
        continue  

    summary = df.describe().to_string()
    insights += f"*Table:* `{table}`\n```\n{summary}\n```\n"

# Post insights to Slack
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
