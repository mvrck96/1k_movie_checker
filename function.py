from urllib.request import urlopen as uReq, quote
from bs4 import BeautifulSoup as soup
import pandas as pd


ivi_url = 'https://www.ivi.ru/search/?q='
megogo_url = 'https://megogo.ru/ru/search-extended?q='

ivi_dict = dict()
megogo_dict = dict()


def search(url, title_dict, container_wrapper, title_wrapper):
    results = []

    client = uReq(url)
    target_page = client.read()
    client.close()

    page_soup = soup(target_page, 'lxml')
    containers = page_soup.findAll(container_wrapper)

    for container in containers:
        found_title = container.findAll(title_wrapper)
        results.append(found_title[0].string.lower())

    if title_dict[url] in results:
        return True
    else:
        return False


def get_titles(file_handler=None):
    if file_handler == None:
        print('File not specified')
    with open(file_handler, 'r') as req:
        titles = req.readlines()
        titles = [_.strip().lower() for _ in titles]
        req.close()
    return titles


target_titles = get_titles('search_list.txt')
result_data = pd.DataFrame({'Ivi': None, 'Megogo': None}, index=target_titles)

for title in target_titles:
    ivi_dict[ivi_url + quote(title)] = title
    megogo_dict[megogo_url + quote(title)] = title

search()