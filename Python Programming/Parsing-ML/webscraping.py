# web scraping is extraction of data from web pages
# most often we need a certain type of data from web pages
# almost all web pages are designed for GUI browser rendering, thus bloated with JS scripts and CSS stlyesheets
# that are less useful & infromative from a web scraping perspective!

# we most often need data wrapped inside specific HTML tags like <table> or <img> or embedded links
# automated web scraping can be helpful in periodic data scraping from websites to make informed decisions or detect trends
# price changes for certain vegetables in selected online stores for a period of 2 years
# temperature/weather patterns in 20 selected locations over a span of 10 years

# beautifulsoup4 module can be used for webscraping with Python

import requests
from bs4 import BeautifulSoup

# lets scrape an HTML table from Wikipedia
# https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate

wiki = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate")

# to get hyperlinks, enclosed by <a> anchor tags
BeautifulSoup(wiki.content, "html.parser")("a")

# to get tables <table>
BeautifulSoup(wiki.content, "html.parser")("table")