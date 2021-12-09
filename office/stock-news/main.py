import requests
from datetime import datetime, timedelta
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#TODO include up or down arrow and percentage in email subject line and message body.

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
    return response.json()['articles']

def send_email(message, ticker):
    my_gmail = "NyetWork001@gmail.com"
    my_yahoo = "NyetWork001@yahoo.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    # connection = smtplib.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        with open("emailpass.txt", "r") as f:
            password = f.read()

        connection.login(my_gmail, password)
        connection.sendmail(from_addr=my_gmail, to_addrs=my_yahoo,
                            msg=f"Subject:{ticker} News Alert\n\n{message}")

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
    data = get_news(COMPANY_NAME)[:3]
    message = ""
    for article in data:
        message += f"{article['title']}\n{article['description']}\n{article['url']}\n\n"
    send_email(message, STOCK)


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

