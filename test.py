from bs4 import BeautifulSoup
import requests

# Fetch the web page
url = "https://www.equitymaster.com/stock-research/financial-data/IEX/INDIAN-ENERGY-EXCHANGE-Detailed-Share-Analysis?utm_source=research-it&utm_medium=website&utm_campaign=factsheet&utm_content=most-viewed"
response = requests.get(url)
data = response.text

# Parse the HTML content
soup = BeautifulSoup(data, 'html.parser')

# Extract specific elements
titles = soup.find_all('h1')
for title in titles:
    print(title.text)
