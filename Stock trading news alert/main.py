import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "2QHZKTQ81WE20I0J"
NEWS_API_KEY = "835b2ca529ae4fec8d89da18823e354a"
account_sid = "ACabbb54a8e2180e90aca7fc7f9035248d"
auth_token = "4330808878630ff5304cfcef2df5fc78"


parameter = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}


responce = requests.get(STOCK_ENDPOINT, params=parameter)
responce.raise_for_status()
data = responce.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday_closing_price = data_list[1]["4. close"]
print(yesterday_closing_price)
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round(difference/float(yesterday_closing_price) * 100)
print(diff_percent)
if abs(diff_percent) >= 3:
    news_param = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_responce = requests.get(NEWS_ENDPOINT, params=news_param)
    article = news_responce.json()["articles"]
    three_article = article[:3]
    # print(three_article)
    formatted_article = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_article]
    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_='+18048854043',
            to='+917083938175'
        )
