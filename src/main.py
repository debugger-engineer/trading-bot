#%%
import os
import sys
import requests
from dotenv import load_dotenv
from tokens import tokens

# === Environment Config # ===
load_dotenv() 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


#%%
def call_coingecko_api(tokens): 
    """
    Fetches historical market data from the CoinGecko API for a dictionary of tokens.

    This function iterates through a dictionary of cryptocurrency tokens, calling the
    CoinGecko API to retrieve the last 60 days of daily market chart data for each.
    It handles API errors gracefully, printing a message for any failed requests
    without stopping the process.

    Args:
        tokens_dict (dict): A dictionary where keys are the CoinGecko API IDs (e.g., "bitcoin")
                          and values are another dictionary containing the token's 'name'
                          and 'symbol'.
        key (str): Your CoinGecko API key for authenticating the requests.

    Returns:
        dict: A dictionary containing the successfully fetched market data. Each key is the
              token's API ID, and the value contains the token's name, symbol, and the
              market data returned by the API. Returns an empty dictionary if no data
              could be fetched.
    """

    market_data = {}

    # Loop through the keys (the api_id) of the dictionary
    for token_id in tokens.keys():

        token_info = tokens[token_id]
        token_name = token_info['name']
        token_symbol = token_info['symbol']

        # API Key config
        api_key = os.getenv("COINGECKO_API_KEY_ACCOUNT1")
        if not api_key:
            raise ValueError("COINGECKO_API_KEY_ACCOUNT1 not found in .env file.")

        # API variables
        url = f"https://api.coingecko.com/api/v3/coins/{token_id}/market_chart"
        api_key = os.getenv("COINGECKO_API_KEY_ACCOUNT1")
        headers = { "x-cg-demo-api-key": api_key }
        parameters = { "vs_currency": "usd", "days": "60", "interval": "daily" }    
        
        response = requests.get(url, headers=headers, params=parameters)
        
        if response.status_code == 200:
            market_data[token_id] = {
                "name": token_name,
                "symbol": token_symbol,
                "market_data": response.json()
            }
        else:
            return print(f"Response status code: {response.status_code}")

    return market_data