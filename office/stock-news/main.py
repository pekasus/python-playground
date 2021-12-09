import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

with open("pass.txt", "r") as f:
    alpha_key = f.read()

with open("pass2.txt", "r") as f:
    news_key = f.read()

def get_news(company):
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": news_key
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    data = response.json()['articles']
    for article in data:
        print(article)


# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo
alpha_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": alpha_key
}

response = requests.get(STOCK_ENDPOINT, params=alpha_params)
data = response.json()['Time Series (Daily)']

now = datetime.now()
yesterday = now - timedelta(days=1)
day_before = now - timedelta(days=2)

yesterday = yesterday.strftime("%Y-%m-%d")
day_before = day_before.strftime("%Y-%m-%d")
yesterday_close = float(data[yesterday]['4. close'])
day_before_close = float(data[day_before]['4. close'])
diff_percent = (abs(yesterday_close - day_before_close)) / yesterday_close

if diff_percent >= 0.005: # DEBUG change to 0.05 for production
    get_news(COMPANY_NAME)


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



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

