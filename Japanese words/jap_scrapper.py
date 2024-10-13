import requests
from bs4 import BeautifulSoup

# Set up the URL and headers
url = 'https://en.wiktionary.org/wiki/Appendix:1000_Japanese_basic_words'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Make the request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table or main content
table = soup.find(name='div', class_='mw-body-content', id='mw-content-text').get_text().strip()

# Split the content at the first occurrence of "Nouns" and take everything after it
if "Nouns" in table:
    table_from_nouns = table.split("Nouns", 1)[1]
    print("Nouns\n" + table_from_nouns)  # Print the content starting from "Nouns"
else:
    print("Could not find 'Nouns' section.")