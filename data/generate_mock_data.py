import random
import faker
import csv

# Initialize the Faker library for generating fake data
fake = faker.Faker()

# Define sample data
customer_names = ['John Doe', 'Jane Smith', 'Alice Brown', 'Bob Johnson', 'Emily Davis', 'Michael Wilson', 'Sarah Taylor']
product_names = ['Laptop', 'Smartphone', 'Headphones', 'Tablet', 'Smartwatch', 'Camera', 'Keyboard']
salesperson_names = ['Alice Smith', 'John Parker', 'Marie White', 'David Lee', 'Sophia Harris']
payment_methods = ['Credit Card', 'Cash', 'Bank Transfer', 'Cryptocurrency']
sales_channels = ['Online', 'In-Store', 'B2B', 'Social Media']
sale_types = ['Retail', 'Wholesale', 'Subscription']
customer_types = ['New', 'Returning', 'VIP']
refund_statuses = ['None', 'Pending', 'Processed', 'Rejected']

# Generate 1,000 rows of data
sales_data = []
for _ in range(20000):
    customer_id = random.randint(1, 100)
    customer_name = random.choice(customer_names)
    product_id = random.randint(1, 20)
    product_name = random.choice(product_names)
    quantity = random.randint(1, 10)
    price = round(random.uniform(50, 2000), 2)
    salesperson_id = random.randint(1, 5)
    salesperson_name = random.choice(salesperson_names)
    payment_method = random.choice(payment_methods)
    region = fake.city()
    sales_channel = random.choice(sales_channels)
    sale_type = random.choice(sale_types)
    customer_type = random.choice(customer_types)
    refund_status = random.choice(refund_statuses)
    order_id = random.randint(1000, 9999)
    sold_at = fake.date_this_decade()

    # Calculate total and final price (assuming 10% discount for some transactions)
    discount = random.choice([0, 5, 10, 15, 20])
    total_price = round(quantity * price, 2)
    final_price = round(total_price * (1 - discount / 100), 2)

    # Append data as a dictionary
    sales_data.append([
        customer_id, customer_name, product_id, product_name, quantity, price,
        salesperson_id, salesperson_name, payment_method, region, sales_channel, sale_type,
        customer_type, refund_status, order_id, sold_at
        # , discount, total_price, final_price
    ])

# Write data to a CSV file (optional)
with open('data/sales_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        'customer_id', 'customer_name', 'product_id', 'product_name', 'quantity', 'price',
        'salesperson_id', 'salesperson_name', 'payment_method', 'region', 'sales_channel', 'sale_type',
        'customer_type', 'refund_status', 'order_id', 'sold_at'
        # , 'discount', 'total_price', 'final_price'
    ])
    writer.writerows(sales_data)

print("20,000 rows of sales data have been generated and written to 'sales_data.csv'.")
