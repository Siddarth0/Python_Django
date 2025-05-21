import requests
from bs4 import BeautifulSoup  # For parsing HTML

# Fetch webpage content
url = "https://www.python.org"  # Replace with the actual webpage URL
response = requests.get(url)

# Parse HTML and extract the title
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string if soup.title else "No title found"

print("Webpage Title:", title)
