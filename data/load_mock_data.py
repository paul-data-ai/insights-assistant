import psycopg2
import json
import csv

# Load config
with open("./config.json", "r") as f:
    config = json.load(f)

# Define connection parameters
db_params = {
    "host": config["db_host"],
    "port": config["db_port"],
    "dbname": config["db_name"],
    "user": config["db_user"],
    "password": config["db_pass"]
}

# Establish the connection to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    print("Connection to PostgreSQL established successfully!")
except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")
    exit()

# Path to the CSV file
csv_file_path = r'C:\Users\HP SPECTRE\projects\data_analysis_llm\data\sales_data.csv'

# Open and load the CSV file into PostgreSQL
try:
    with open(csv_file_path, 'r') as csv_file:
        # Skip the header row in the CSV file
        next(csv_file)

        # Use COPY command to load data into the sales table
        cursor.copy_from(csv_file, 'sales', sep=',', columns=(
            'customer_id', 'customer_name', 'product_id', 'product_name', 'quantity', 
            'price', 'salesperson_id', 'salesperson_name', 'payment_method', 'region', 
            'sales_channel', 'sale_type', 'customer_type', 'refund_status', 'order_id', 
            'sold_at'
        ))

    # Commit the transaction
    connection.commit()
    print(f"Data successfully loaded into 'sales' table from {csv_file_path}.")

except Exception as e:
    print(f"Error loading data from CSV: {e}")
    connection.rollback()

# Close the connection
cursor.close()
connection.close()
