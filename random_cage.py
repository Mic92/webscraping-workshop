#!/usr/bin/env python
import requests, random
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Nicolas_Cage_filmography"
doc = requests.get(url)
soup = BeautifulSoup(doc.text, 'html.parser')
rows = soup.select("table.wikitable.sortable tr")
choice = random.choice(rows)
print(choice.select("td i a")[0].text)
