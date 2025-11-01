import os
import sys
import requests
from dotenv import load_dotenv
from pathlib import Path

# Explicity set the .env file path
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def send_telegram_message(message):
    """
    Sends a message to a specified Telegram chat.

    Args:
        message (str): The text message to send.

    Returns:
        dict: The JSON response from the Telegram API.
    """

    # Load secrets from .env file
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_id:
        print("Error: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set in the .env file.")
        return {"ok": False, "description": "Environment variables not set."}
    
    # Send the message via Telegram API
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending Telegram message: {e}")
        return {"ok": False, "description": str(e)}

# For testing purposes
if __name__ == "__main__":
    load_dotenv()
    test_data = send_telegram_message("Hello, World!")