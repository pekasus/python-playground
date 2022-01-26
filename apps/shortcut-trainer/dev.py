import json

data = json.load(open('tools/cheat-codes.json'))

print(data['topics']['command-line'].keys())