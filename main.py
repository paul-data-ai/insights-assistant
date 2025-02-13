import os
import pandas as pd
import json
import requests
from datetime import datetime
from sqlalchemy import create_engine

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

# Create SQLAlchemy engine for PostgreSQL connection
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

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

# Send to Slack if the URL is set
if SLACK_WEBHOOK_URL:
    requests.post(SLACK_WEBHOOK_URL, json={"text": insights})
    print("✅ Insights sent to Slack!")
else:
    print("❌ SLACK_WEBHOOK_URL is not set.")
