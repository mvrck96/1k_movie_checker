from math import nan
from urllib.request import quote
from urllib.request import urlopen as uReq

import pandas as pd
from bs4 import BeautifulSoup as soup

ivi_url = 'https://www.ivi.ru/search/?q='
megogo_url = 'https://megogo.ru/ru/search-extended?q='

ivi_dict = dict()
megogo_dict = dict()


def ivi_search(url):
    client = uReq(url)
    target_page = client.read()
    client.close()

    page_soup = soup(target_page, 'lxml')
    containers = page_soup.findAll('li', {'class': 'gallery__item'})

    results = []

    for container in containers:
        found_title = container.findAll(
            'div', {'class': 'nbl-slimPosterBlock__title'})
        results.append(found_title[0].string.lower())

    if ivi_dict[url] in results:
        result_data.loc[ivi_dict[url], 'Ivi'] = 'Есть'
    else:
        result_data.loc[ivi_dict[url], 'Ivi'] = 'Нет'


def megogo_search(url):
    client = uReq(url)
    target_page = client.read()
    client.close()

    page_soup = soup(target_page, 'lxml')
    containers = page_soup.findAll('div', {
        'class': 'card videoItem direction-vertical orientation-portrait '
                 'size-normal type-normal'})

    results = []

    for container in containers:
        buffer = str(container['title'])
        results.append(buffer.lower())

    if megogo_dict[url] in results:
        result_data.loc[megogo_dict[url], 'Megogo'] = 'Есть'
    else:
        result_data.loc[megogo_dict[url], 'Megogo'] = 'Нет'


def table_manager(dict1, dict2):
    for key in dict1:
        ivi_search(key)
    for key in dict2:
        megogo_search(key)
    result_data.to_csv('result.csv', index_label='Title')
    return result_data


with open('search_list.txt', 'r') as req:
    titles = req.readlines()
    titles = [_.strip().lower() for _ in titles]
    req.close()

for title in titles:
    ivi_dict[ivi_url + quote(title)] = title
    megogo_dict[megogo_url + quote(title)] = title

result_data = pd.DataFrame({'Ivi': nan, 'Megogo': nan}, index=titles)

table_manager(ivi_dict, megogo_dict)
