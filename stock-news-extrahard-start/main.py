import requests
from datetime import datetime, timedelta
import itertools

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

now = datetime.now()
yesterday = datetime.now() - timedelta(days=1)
two_days_ago = datetime.now() - timedelta(days=2)

todays_date = now.strftime("%Y-%m-%d")
yesterdays_date = yesterday.strftime("%Y-%m-%d")
two_days_ago_date = two_days_ago.strftime("%Y-%m-%d")

stock_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": "9EJ5MQME0GTHRXYG"
}

news_parameters = {
    "q": COMPANY_NAME,
    "from": yesterdays_date,
    "sortBy": "popularity",
    "apiKey": "7ef5d319325147e8a38f083fbed96704"
}

stock_reponse = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_reponse.raise_for_status()

news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()

data = stock_reponse.json()

yesterdays_price = float(data["Time Series (60min)"][f"{yesterdays_date}" + " 19:00:00"]["4. close"])
two_days_ago_price = float(data["Time Series (60min)"][f"{two_days_ago_date}" + " 19:00:00"]["4. close"])

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
percentage_change = abs((yesterdays_price - two_days_ago_price) / two_days_ago_price) * 100

if percentage_change >= 5:
    print("Get News")

# percentage_change = 6

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

the_news = news_response.json()
first3vals = the_news['articles'][:3]


# if percentage_change >=5:
#     print(first3vals["articles"])

#print(first3vals)
if percentage_change >= 5:
    if yesterdays_price > two_days_ago_price:
        for article in first3vals:
            print(f"{STOCK}: 🔺{percentage_change}%\nHeadline: {article["title"]}\nBrief: {article["description"]}")
    elif yesterdays_price < two_days_ago_price:
        for article in first3vals:
            print(f"{STOCK}: 🔺{percentage_change}%\nHeadline: {article["title"]}\nBrief: {article["description"]}")


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Twilio integration is broken. Can't do this step. However, if we could, the printed output would suffice as challenge completion.

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

