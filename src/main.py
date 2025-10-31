#%%
import os
import sys
import requests
from dotenv import load_dotenv
from tokens import tokens

#%%
load_dotenv() 

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

api_key = os.getenv("COINGECKO_API_KEY_ACCOUNT1")
if not api_key:
    raise ValueError("COINGECKO_API_KEY_ACCOUNT1 not found in .env file.")

#%%
headers = { "x-cg-demo-api-key": api_key }
parameters = { "vs_currency": "usd", "days": "60", "interval": "daily" }

#%%
# Empty dictionary to store the api response
market_data = {}

# Loop through the keys (the api_id) of the dictionary
for token_id in tokens.keys():

    token_info = tokens[token_id]
    token_name = token_info['name']
    token_symbol = token_info['symbol']

    url = f"https://api.coingecko.com/api/v3/coins/{token_id}/market_chart"
        
    response = requests.get(url, headers=headers, params=parameters)
    
    print(response.json())


    if response.status_code == 200:
        market_data[token_id] = {
            "name": token_name,
            "symbol": token_symbol,
            "market_data": response.json()
        }
    else:
        print(f"Response status code: {response.status_code}")




# %%
print(market_data)
# %%
