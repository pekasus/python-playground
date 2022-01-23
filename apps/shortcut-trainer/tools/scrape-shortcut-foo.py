import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

json_file = 'cheat-codes.json'
topics = ['command-line', 'sublime-text-3-win', 'vscode-win', 'pycharm-win', 'git', 'tmux',
          'python-regex', 'qutebrowser', 'python-strings', 'javascript-strings', 'javascript-arrays', 'regex',
          'photoshop-win', 'atom-mac', 'sublime-text-3-mac', 'chrome-dev-tools-mac', 'photoshop-mac', 
          'vscode-mac', 'pycharm-mac']

with open(json_file, 'w') as f:
    f.write('{"contents":[], "topics":{}}')

driver = webdriver.Firefox()

for topic in topics:
    url = f"https://www.shortcutfoo.com/app/dojos/{topic}/cheatsheet"
    driver.get(url)
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'plans-section-header'))
    WebDriverWait(driver, 20).until(element_present)

    sections = driver.find_elements(By.CLASS_NAME, 'plans-section-header')
    tables = driver.find_elements(By.CLASS_NAME, 'shortcuts-container')
    joint = list(zip(sections, tables))

    data = {}

    for j in joint:
        heading = j[0].text
        data[heading] = {}
        containers = j[1].find_elements(By.CLASS_NAME, "cheatsheet-shortcut-container")
        for c in containers:
            key = c.find_element(By.CLASS_NAME, "cheatsheet-keys").text
            command = c.find_element(By.CLASS_NAME, "cheatsheet-name").text
            data[heading][key] = command

    data_json = json.load(open("cheat-codes.json"))
    data_json['topics'][topic] = data
    data_json['contents'].append(topic)

    print(data_json)

    with open(json_file, 'w') as f:
        json.dump(data_json, f)

    time.sleep(10)

driver.quit()