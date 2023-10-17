import requests
from bs4 import BeautifulSoup

url = "https://example.com/products"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
prices = soup.find_all("span", class_="price")
for price in prices:
    print(price.text)
    


