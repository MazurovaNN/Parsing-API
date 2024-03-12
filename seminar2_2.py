import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint

url = "https://gb.ru"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
#params = {'page': 1}

session = requests.session()

response = session.get(url+"/posts", headers=headers) #, params=params)
soup = BeautifulSoup(response.text, "html.parser")

post = soup.find_all('div', {'class':'post-item'})
print()

#all_posts = []
#for post in posts:
 #   post_info = {}

 #   name_info = post.find('div',{'class':'post-item event'})
 #  post_info['name'] = name_info.getText()
 #   post_info['url'] = url+name_info.get('href')




