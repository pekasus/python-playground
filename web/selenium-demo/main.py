from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=s)

# driver.get('https://www.amazon.com/dp/B0932FPBV8/?_encoding=UTF8&psc=1')
# price = driver.find_element(By.CLASS_NAME, "apexPriceToPay")
# print(price.text)

driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)



driver.close() # Closes a tab
driver.quit() # Quits the browser




