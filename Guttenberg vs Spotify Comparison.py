import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import csv

# Define the headers for the CSV file
headers = ['Guttenberg Title', 'Guttenberg Author', 'Guttenberg URL']

with open('Guttenberg vs Spotify Comparison.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write the headers to the CSV file
    
    def get_titles_and_author(page_no):
        url = f'https://www.gutenberg.org/ebooks/{page_no}'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        all_titles = soup.find('h1').text.strip()
        titles = all_titles.split(' by ')[0]
        author = all_titles.split(' by ')[-1]
        return titles, author

    # Starting page number
    page_no = 1

    # Loop to run the function 3 times
    for _ in range(10):
        titles, author = get_titles_and_author(page_no)
        url = f"https://www.gutenberg.org/ebooks/{page_no}"
        page_no += 1
        writer.writerow([titles, author, url])