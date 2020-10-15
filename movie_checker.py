import pandas as pd
from urllib.request import quote
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

THEATER_DICT = {
    'megogo': ['https://megogo.ru/ru/search-extended?q=',('h3', 'video-title')],
    'okko': ['https://okko.tv/search/', ('span', '_7NsSm')],
    'tnt': ['https://premier.one/search?query=', ('div', 'slider-title')],
    'tvigle': ['https://www.tvigle.ru/search/?q=', ('div', 'product-list__item_name')],
    'wink': ['https://wink.rt.ru/search?query=', ('h4', 'root_r1ru04lg title_tyrtgqg root_subtitle2_r18emsye')],
}


def search(title: str, theater_handler: str) -> bool:

    meta = THEATER_DICT.get(theater_handler)
    title = title.lower().strip()
    target_url = THEATER_DICT.get(theater_handler)[0] + quote(title)

    client = uReq(target_url)
    target_page = client.read()
    client.close()

    page_soup = soup(target_page, 'lxml')
    containers = page_soup.findAll(meta[1][0],{'class': meta[1][1]})
    founded_titles = [container.text.strip().lower() for container in containers]
    result = False

    if title in founded_titles:
        result = True
    else:
        results = False
    return result


def get_titles(file_handler=None) -> list:

    with open(file_handler, 'r') as f:
        titles = [title.strip() for title in f.readlines()]
    return titles


def search_manager(titles: list) -> pd.DataFrame:

    table = pd.DataFrame(index=titles)
    for key in THEATER_DICT:
        result = [search(title, key) for title in titles]
        table[key] = result
    return table


if __name__ == '__main__':
    # todo: Сделать инликацию прогресса поиска фильмов. Что бы было понятно как идет процесс
    movies_to_find = get_titles('search_list.txt')
    df = search_manager(movies_to_find)
    df.to_csv('result.csv')

