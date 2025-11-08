import os
import requests
from twilio.rest import Client
import random
from dotenv import load_dotenv

# PROGRAM PURPOSE:
# This script monitors the daily stock price of a company
# (in this case Tesla Inc) using the Alpha Vantage API.
# If the stock price changes significantly, it retrieves
# recent news articles about the company via the NewsAPI
# and sends one of them to your phone through Twilio.

# Target stock and company name to analyse
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Load and retrieve environment variables from the local .env file.
load_dotenv()
twilio_account_sid = os.getenv("TWILIO_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
news_api = os.getenv("NEWS_API_KEY")
stock_api = os.getenv("STOCK_API_KEY")
from_number = os.getenv("FROM_NUMBER")
to_number = os.getenv("TO_NUMBER")

# Define the endpoints for each API service
# NewsAPI provides recent related news articles.
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# Alpha Vantage provides stock price data,
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

# Retrieve recent news articles about the chosen company.
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": news_api
}
news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

# Retrieve recent daily stock data from Alpha Vantage.
# The "Time Series (Daily)" function returns a dictionary
# containing daily open, high, low, close, and volume data.
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (Daily)']

# STEP 1: Determine the recent stock price change.
# The goal is to calculate the percentage difference
# between yesterday's closing price and the previous day's.
stock_data_list = [value for (key,value) in stock_data.items()]

# Note: The latest entries are at index 0 and 1.
# Be aware that weekends and holidays may produce missing data.
yesterday_close = float(stock_data_list[0]['4. close'])
two_days_ago_close = float(stock_data_list[1]['4. close'])

# Calculate percentage difference and round to one decimal place.
percentage_difference = round(((yesterday_close-two_days_ago_close)/yesterday_close)*100,1)

# Determine whether price rose, fell, or stayed stable.
if percentage_difference > 0:
    sign = "+"
elif percentage_difference < 0:
    sign = "-"
else:
    sign = "~"

# STEP 2: Retrieve and prepare the company news articles.
# If the price change meets your condition (currently >= 0), the program selects a random article from the first three.
if abs(percentage_difference) >= 0:
    # Collect the first three articles (if available)
    article_list = [news_data["articles"][index] for index in range(0,3)]

    # Pick one article at random to include in the message
    random_article = random.choice(article_list)

    # Construct the message body with stock change and article details
    message_to_send = (
        f"{STOCK}: {sign}{percentage_difference}%\n"
        f"Headline: {random_article['title']}\n"
        f"Brief: {random_article['description']}"
    )

    # STEP 3: Send the alert using Twilio.
    # This uses the Twilio REST API client to send a message to specified whatsapp number
    client = Client(twilio_account_sid,twilio_auth_token)
    message = client.messages \
    .create(
        body=message_to_send,
        from_= from_number,
        to= to_number
    )
    # Print Twilio's message SID for confirmation
    print(message.sid)