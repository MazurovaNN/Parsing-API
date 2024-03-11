import os
import requests
import json
from dotenv import load_dotenv
from pprint import pprint
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

url = "https://api.giphy.com/v1/gifs/search"
params = {
    "api_key": os.getenv("API_KEY"),
    "q": "programming",
    "limit": 5,
    "offset": 0,
    "rating": "g",
    "lang": "ru",
    "bundle": "messaging_non_clips",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "*/*",
}
# Запрос на сервер
response = requests.get(url, params=params, headers=headers)
j_data = response.json()

with open('gifs.json', 'w') as f:
    json.dump(j_data, f)

for gif in j_data.get('data'):
    print(gif.get('images').get('original').get('url'))

pprint(j_data)








