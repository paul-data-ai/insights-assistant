import os
import pandas as pd
import psycopg2
import requests
import json
from datetime import datetime

# # Get secrets from environment variables 
# DB_HOST = os.getenv("DB_HOST")
# DB_USER = os.getenv("DB_USER")
# DB_PASS = os.getenv("DB_PASS")
# DB_NAME = os.getenv("DB_NAME")
# DB_PORT = os.getenv("DB_PORT")  # Default PostgreSQL port
# SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK")

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

# Get secrets from environment variables
DB_HOST = config["db_host"]
DB_USER = config["db_user"]
DB_PASS = config["db_pass"]
DB_NAME = config["db_name"]
DB_PORT = config["db_port"]  # Default PostgreSQL port
SLACK_WEBHOOK_URL = config["slack_webhook"]

connection_string = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    conn = psycopg2.connect(connection_string)
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    dbname=DB_NAME,
    port=DB_PORT
)

# Get all tables in the public schema
query = "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';"
tables = pd.read_sql(query, conn)

insights = f"📊 *Auto-Generated Data Insights* 📊\n📅 {datetime.now().strftime('%Y-%m-%d %H:%M')} \n\n"

# Analyze each table
for table in tables["tablename"]:
    data_query = f"SELECT * FROM {table} LIMIT 1000"
    df = pd.read_sql(data_query, conn)

    if df.empty:
        continue  

    summary = df.describe().to_string()
    insights += f"*Table:* `{table}`\n```\n{summary}\n```\n"

# Close DB connection
conn.close()

# Send to Slack
requests.post(SLACK_WEBHOOK_URL, json={"text": insights})

print("✅ Insights sent to Slack!")
