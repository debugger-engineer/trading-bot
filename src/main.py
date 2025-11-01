#%%
# Standard Library Imports
import os
import sys
from pathlib import Path

# Third-Party Library Imports
from dotenv import load_dotenv

# --- Setup Paths and Environment ---
# This block should come BEFORE your application imports.
sys.path.append(str(Path(__file__).parent))
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Your Application's Imports
import functions
from telegram_bot import send_telegram_message
from tokens import tokens


def main():

    # Call CoinGecko API
    print("Calling CoinGecko API...")
    market_data = functions.call_coingecko_api(tokens)
    if not market_data:
        print("Error: Failed to fetch market data from CoinGecko API.")
    print(f"Fetched {len(market_data)} tokens.")
    
    # Calculate RSI
    print("Calculating RSI...")
    rsi_value = functions.calculate_rsi(market_data)
    if not rsi_value:
        print("Error: Failed to calculate RSI.")
        return
    print(f"RSI values: {rsi_value}")

    # Check for oversold tokens and send Telegram alerts
    print("Checking for oversold tokens (RSI < 60)...")
    for symbol, data in rsi_value.items():
        rsi = data.get('rsi')
        if rsi is not None and rsi < 60:
            print(f"Sending Telegram alert for {symbol} with RSI {rsi}...")

            message = (
                f"🚨 *Oversold Alert!* 🚨\n\n"
                f"**Token:** {symbol}\n"
                f"**RSI:** {rsi:.2f}\n\n"
                f"This is an automated alert."
            )

            send_telegram_message(message)
        elif rsi is None:
            print(f"Could not calculate RSI for {symbol}.")

    print("--- Market check complete ---")



if __name__ == "__main__":
    main()