'''
Install packages
pip install requests
pip install beautifulsoup4
'''
import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")

print(soup.title)
print(soup.title.get_text())
print(soup.body)