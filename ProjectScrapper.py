from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('./chromedriver')

browser.get(START_URL)
time.sleep(5)

headers = ["Proper name", "Distance (ly)", "Mass (M☉)", "Radius (R☉)", "Luminosity (L☉)"]

soup = BeautifulSoup(browser.page_source, "html.parser")

table = soup.find('table')
table_rows = table.find_all(['tr'])[1:]

with open("Scrapped Data Of Stars.csv", "w", encoding = "utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for rows in table_rows:
        table_data = rows.find_all('td')
        row = [data.text.replace('\n','') for data in table_data]
        writer.writerow(row)