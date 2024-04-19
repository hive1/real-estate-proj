import requests
from bs4 import BeautifulSoup

zipcode = 11934

url = f"https://www.redfin.com/zipcode/{zipcode}"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.prettify())

