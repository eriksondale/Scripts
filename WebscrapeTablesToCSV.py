import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv

url = input("Enter Secure URL: ")
# Create a handle, page, to handle the contents of the website
# Store the contents of the website under soup
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page = requests.get(url, headers=headers)
print("Fetching Page Data...............")
print(page)
print("-----------------------------------")
soup = BeautifulSoup(page.content, 'lxml')

# Parse data that is stored in tables
tables = soup.find_all('table')
print(tables)

try:
    url = url.replace("/", "")
    url = url.replace("https:", "")
    url = url.replace(".com", "")
except:
    pass
url = url + ".csv"
for table in tables:
    print(table)
    table = pd.read_html(table)
    print("----------")
    print(table)
    print("----------")
