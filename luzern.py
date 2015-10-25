#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import sqlite3


def store_lots(lots):
    conn = sqlite3.connect('lots.db')
    sql = '''
    CREATE TABLE IF NOT EXISTS free_lots (
        created_at timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
        name text,
        free integer)
    '''
    c = conn.cursor()
    c.execute(sql)
    for name, free_lots in lots:
        sql = "INSERT INTO free_lots(name, free) values (?, ?)"
        c.execute(sql, (name, free_lots))
    conn.commit()
    conn.close()


def scrape_lots(soup):
    lots = []
    rows = soup.select(".parking-list .parking-station")
    for row in rows:
        name = row.select(".name")[0].text
        free_spaces = row.select(".free-spaces")[0].text
        lots.append((name, int(free_spaces),))
    return lots


def main():
    url = "http://www.pls-luzern.ch/de/"
    doc = requests.get(url)
    soup = BeautifulSoup(doc.text, 'html.parser')
    #html = open("/tmp/Parkleitsystem.html").read()
    #soup = BeautifulSoup(html, 'html.parser')

    lots = scrape_lots(soup)
    for name, free_lots in lots:
        print("%s: %s" % (name, free_lots))

    store_lots(lots)

if __name__ == "__main__":
    main()
