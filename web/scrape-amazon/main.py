import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4707.0 Safari/537.36"
}

html = requests.get("https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=dp_prsubs_2?pd_rd_i=B08PQ2KWHS&psc=1", headers=headers).text
soup = BeautifulSoup(html, "lxml")
prices = soup.find(name="span", class_="apexPriceToPay")
price = float(prices.text.split("$")[1])