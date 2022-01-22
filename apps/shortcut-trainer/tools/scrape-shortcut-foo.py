from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

topic = 'vim'
url = f"https://www.shortcutfoo.com/app/dojos/{topic}/cheatsheet"

driver = webdriver.Firefox()
driver.get(url)

full_table = driver.find_element(By.CLASS_NAME, 'units-container')
sections = full_table.find_elements(By.CLASS_NAME, 'plans-section-header')
tables = full_table.find_elements(By.CLASS_NAME, 'shortcuts-container')
joint = list(zip(sections, tables))

data = {}
data[topic] = {}
data_topic = data[topic]

for j in joint:
    heading = j[0].text
    data_topic[heading] = {}
    containers = j[1].find_elements(By.CLASS_NAME, "cheatsheet-shortcut-container")
    for c in containers:
        key = c.find_element(By.CLASS_NAME, "cheatsheet-keys").text
        command = c.find_element(By.CLASS_NAME, "cheatsheet-name").text
        data_topic[heading][key] = command

data['contents'].append(topic)

data_json = json.load(open("cheat-codes.json"))
with open(f'cheat-codes.json', 'w') as f:
    json.dump(data, f)