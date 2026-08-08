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

#Find HTML elements:

'Find all the tables in the HTML document'
tables = soup.find_all("table")

'Find by tag + attribute:'
tables = soup.find_all("table", {"cellpadding": "3"})

'Find one:'
table = soup.find("table")

'Find rows:'
rows = table.find_all("tr")