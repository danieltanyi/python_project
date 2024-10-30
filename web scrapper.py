"""Project 6
Problem Statement:
The task is to scrape the list of largest companies in US by revenue form wikipedia using Beautiful Soup in Python. The data required to be extracted includes the rank, name of company, Industry, Revenue, Revenue growth, Headquaters.

Question:
What is the process to extract data from the wikipedia website using Beautiful Soup in Python? Specifically, how can we extract the rank, name of the company, Industry, Revenue, Revenue growth, Headquarters for the top US companies by Revenue?"""

### Libraries Installation
# !pip install requests
# !pip install beautifulsoup4

import requests

from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
print(soup.prettify)



