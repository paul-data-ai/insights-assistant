import os
import json
import requests

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

SLACK_WEBHOOK_URL = config["slack_webhook"]

message = {
    "text": "🚀 Hello from GitHub Actions! This is a test message."
}

response = requests.post(SLACK_WEBHOOK_URL, json=message)

if response.status_code == 200:
    print("✅ Message sent successfully!")
else:
    print(f"❌ Failed to send message. Status Code: {response.status_code}, Response: {response.text}")
