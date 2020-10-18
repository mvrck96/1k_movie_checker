import pandas as pd
from urllib.request import quote
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import argparse
import os

THEATER_DICT = {
    'megogo': ['https://megogo.ru/ru/search-extended?q=',('h3', 'video-title')],
    'okko': ['https://okko.tv/search/', ('span', '_7NsSm')],
    'tnt_premier': ['https://premier.one/search?query=', ('div', 'slider-title')],
    'tvigle': ['https://www.tvigle.ru/search/?q=', ('div', 'product-list__item_name')],
    'wink': ['https://wink.rt.ru/search?query=', ('h4', 'root_r1ru04lg title_tyrtgqg root_subtitle2_r18emsye')],
}


def search(title: str, theater_handler: str) -> bool:
    """
    Check if online movie theater have specified movie.

    Checking is performed with parsing the HTML file addressed with url from THEATER_DICT.
    If given title could be found on this page true value returned, if not than false.

    Parameters
    ----------
    title: str, movie to found
    theater_handler: str, handler of theater to find in. Can be found in THEATER_DICT

    Returns
    -------
    Bool
        True if movie was found, false if wasn't
    """
    meta = THEATER_DICT.get(theater_handler)
    title = title.lower().strip()
    target_url = THEATER_DICT.get(theater_handler)[0] + quote(title)

    client = uReq(target_url)
    target_page = client.read()
    client.close()

    page_soup = soup(target_page, 'lxml')
    containers = page_soup.findAll(meta[1][0],{'class': meta[1][1]})
    founded_titles = [container.text.strip().lower() for container in containers]
    result = True if title in founded_titles else False
    return result

def get_titles(file_handler=None) -> list:
    """
    Get movie titles from the specified .txt file

    Parameters
    ----------
    file_handler: str, file with titles

    Returns
    -------
    List
        List of parsed titles
    """
    with open(file_handler, 'r') as f:
        titles = [title.strip() for title in f.readlines()]
    return titles


def search_manager(titles: list, movie: str) -> pd.DataFrame:
    """
    Perform search and makes a table with search results

    Parameters
    ----------
    titles: list, list of movie titles to search
    movie: str, single movie to find
    Returns
    -------
    Table
        pd.DataFrame, result table
    """

    if movie:
        table = pd.DataFrame(index=[movie])
        for key in THEATER_DICT:
            table[key] = search(movie, key)
        print(table.head())
    else:
        table = pd.DataFrame(index=titles)
        for key in THEATER_DICT:
            result = [search(title, key) for title in titles]
            table[key] = result
    return table


if __name__ == '__main__':
    # todo: Сделать индикацию прогресса поиска фильмов. Что бы было понятно как идет процесс
    # todo: Добавить обработчик запуска с параметром

    parser = argparse.ArgumentParser()
    parser.add_argument("--movie", type=str)
    args = parser.parse_args()
    single_movie = args.movie

    movies_to_find = get_titles('search_list.txt')
    search_manager(movies_to_find, single_movie).to_csv('result.csv')

    print(f"Done !")

