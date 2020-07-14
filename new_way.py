from urllib.request import urlopen as uReq, quote
from bs4 import BeautifulSoup as soup
import pandas as pd
from multiprocessing import Pool

ivi_manager = {'url': 'https://www.ivi.ru/search/?q=',
               'handler': 'ivi'}
ivi_container_wrapper = ('nbl-slimPosterBlock__textSection')
ivi_title_wrapper = 'nbl-slimPosterBlock__title'


def search(url, title, theater_handler, container_wrapper, title_wrapper):
    results = list()

    client = uReq(url)
    target_page = client.read()
    client.close()

    page_soup = soup(target_page, 'html.parser')

    containers = page_soup.find_all(container_wrapper)

    for container in containers:
        found_title = container.find(title_wrapper)
        results.append(found_title.string.lower())

    if title in results:
        print('{0} есть в {1}'.format(title, theater_handler))
    else:
        print('{0} нет в {1}'.format(title, theater_handler))


movie_title = 'офицеры'
movie_url = 'https://www.ivi.ru/search/?q={0}'.format(quote('офицеры'))

search(movie_url, movie_title, ivi_manager['handler'],ivi_container_wrapper, ivi_title_wrapper)