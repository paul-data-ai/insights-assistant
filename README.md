# Insights Assistant

Insights Assistant is an AI-powered data analysis tool designed to fetch, analyze, and visualize sales data insights. The insights are auto-generated (based on interested metrics) and can be sent to various communication platforms such as Slack, Discord, Microsoft Teams, and more.

## Some predefined Questions

- **Total Sales by Payment Method**: Analyze sales data based on different payment methods.
- **Top Selling Products**: Identify the top-selling products in your inventory.
- **Sales Performance by Region**: Evaluate sales performance across different regions.
- **Customer Type Analysis**: Understand the distribution of customer types.
- **Sales Channel Comparison**: Compare sales performance across various sales channels.
- **Sales Trend Over Time**: Observe sales trends over time (daily).
- **Sales Performance by Salesperson**: Monitor the performance of individual salespersons.
- **Actionable Insights**: Generate actionable insights and send them to a specified communication platform.

## Future Goals

- **Multi-Platform Support**: Expand the tool to support various communication platforms such as Discord, Microsoft Teams, and more.
- **User-Generated Queries**: Enable users to input custom queries and receive auto-generated insights based on their questions.
- **Enhanced AI Capabilities**: Incorporate advanced AI models to provide deeper insights and more accurate predictions.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/paul-data-ai/insights-assistant.git
    cd insights-assistant
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following environment variables:
    ```
    DB_HOST = ****************
    DB_USER = ****************
    DB_PASS = ****************
    DB_NAME = ****************
    DB_PORT = ****************
    
    # slack
    SLACK_WEBHOOK_URL = ****************
    SLACK_BOT_TOKEN = ****************
    SLACK_CLIENT_ID = ****************
    SLACK_CLIENT_SECRET = ****************
    SLACK_SIGNING_SECRET = ****************
    
    
    # TOGETHER API
    TOGETHER_API_KEY = ****************
    
    # email
    EMAIL_SENDER = ****************@gmail.com
    EMAIL_PASSWORD = ****************
    EMAIL_RECIPIENT = ****************
    SMTP_SERVER = smtp.gmail.com
    SMTP_PORT = 587
    ```

4. **Set up the database connection**:
    Ensure you have a database credentials set up and update the connection settings in `database/conn.py`.

## Usage

1. **Run the main script**:
    ```bash
    python main.py
    ```

2. The script will fetch and analyze sales data, generate insights, and send them to the specified communication platform.

## Project Structure

- `main.py`: The main script to fetch, analyze, and send insights.
- `database/conn.py`: Database connection setup.
- `insights/queries.py`: Code to fetch data.
- `insights/charts.py`: Functions to generate visualizations.
- `llm/llm.py`: Function to generate actionable insights.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
