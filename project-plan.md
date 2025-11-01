# Trading Bot Project Plan

A agent/bot to monitor the crypto market, send alerts when a token is oversold (oportunity) and open/close orders in a perpetuals exchange via commands on telegram bot

## Completed
- [x] Function to call CoinGecko API and fetch market data.

## Next Steps
- [ ] Implement RSI (Relative Strength Index) calculation.
- [ ] Make the function call_coingecko_api smarter by saving the call results in a sql lite db and calling only the missing values (like today's values), not all the values in every call.
- [ ] Integrate with a Telegram bot for sending alerts.
- [ ] Integrate with a cryptocurrency exchange API to place trade orders.
