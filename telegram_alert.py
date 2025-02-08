import requests
import pandas as pd

# Replace with your Telegram bot token and chat ID
telegram_bot_token = "your_telegram_bot_token"
telegram_chat_id = "your_chat_id"

# Load AI recommendations
ai_trades_df = pd.read_csv("ai_recommendations.csv")

def send_telegram_alert(message):
    telegram_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    data = {"chat_id": telegram_chat_id, "text": message}
    requests.post(telegram_url, data=data)

# Format message
alert_message = "📊 AI Trade Recommendations:\n" + ai_trades_df.to_string()

# Send alert
send_telegram_alert(alert_message)
