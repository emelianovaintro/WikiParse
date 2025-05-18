import csv

import requests
from bs4 import BeautifulSoup


def get_table(url):
    response = requests.get(url)
    if response.status_code != 200:
        exit()

    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table', {'class': 'wikitable'})

    if not tables:
        return None

    return tables[0]


def get_data(table):
    rows = table.find_all('tr')[1:]
    data = []

    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 4:
            code = cells[0].text.strip()
            nums = cells[1].text.strip()
            currency = cells[3].text.strip()
            data.append([code, nums, currency])

    return data


def save_data_to_csv(data):
    with open('currencies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Code', 'Nums', 'Currency'])

        for row in data:
            writer.writerow(row)
