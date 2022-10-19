import requests
import itertools
from twilio.rest import Client

twilio_account_sid = "your sid"
twilio_auth_token = "your token"

STOCK = "stock name"
COMPANY_NAME = "Tesla Inc"

my_price_api_key = "your price api"
my_news_api_key = "your news api"

price_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": my_price_api_key
}

news_params = {
    "q": COMPANY_NAME,
    "apiKey": my_news_api_key
}

response = requests.get(url="https://www.alphavantage.co/query", params=price_params)
response.raise_for_status()
price_data = response.json()
daily_prices = price_data["Time Series (Daily)"]

two_days = dict(itertools.islice(daily_prices.items(), 2))

my_data_list = [float(value["4. close"]) for _, value in two_days.items()]

ratio = (my_data_list[0]-my_data_list[1])*100/my_data_list[1]
ratio = float("{:.2f}".format(ratio))

print(ratio)

if ratio > 5.0 or ratio < -5.0:

    response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    response.raise_for_status()
    news = response.json()["articles"][:3]

    for action in news:
        title = action["title"]
        description = action["description"]

        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages.create(
            body=f"Headline: {title}\n Brief: {description}.",
            from_='twilio number',
            to='your number'
        )

        print(message.status)



