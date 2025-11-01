import time
import schedule
import functions
from telegram_bot import send_telegram_message
from tokens import tokens

class CheckMarketsHourly:
    def __init__(self):
        print("Initializing the hourly market check process...")
        self.tokens_to_watch = tokens

    def run_market_check(self):
        print("\n--- [Scheduled Job] Starting Market Check ---")
        
        market_data = functions.call_coingecko_api(self.tokens_to_watch)
        if not market_data:
            print("Could not fetch market data.")
            return

        rsi_values = functions.calculate_rsi(market_data)
        if not rsi_values:
            print("Could not calculate RSI.")
            return

        print(f"RSI values calculated: {rsi_values}")

        oversold_num = 30
        for symbol, data in rsi_values.items():
            rsi = data.get('rsi')
            if rsi is not None and rsi < oversold_num:
                print(f"ALERT: {symbol} is oversold with RSI: {rsi}")
                message = (
                    f"🚨 *Oversold Alert!* 🚨\n\n"
                    f"**Token:** {symbol}\n"
                    f"**RSI:** {rsi:.2f}"
                )
                send_telegram_message(message)
        
        print("--- [Scheduled Job] Market Check Complete ---")

    def start(self):
        print("Process is now running. Press Ctrl+C to exit.")
        
        schedule.every().hour.do(self.run_market_check)
        
        self.run_market_check()

        while True:
            schedule.run_pending()
            time.sleep(1)