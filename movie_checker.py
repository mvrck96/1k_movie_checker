import pandas as pd
from urllib.request import quote
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from typing import Tuple
from progress.bar import FillingCirclesBar

import argparse
import os

THEATER_DICT = {
    'Megogo': ['https://megogo.ru/ru/search-extended?q=',('h3', 'video-title')],
    'Okko': ['https://okko.tv/search/', ('span', '_7NsSm')],
    'Tnt_premier': ['https://premier.one/search?query=', ('div', 'slider-title')],
    'Tvigle': ['https://www.tvigle.ru/search/?q=', ('div', 'product-list__item_name')],
    'Wink': ['https://wink.rt.ru/search?query=', ('h4', 'root_r1ru04lg title_tyrtgqg root_subtitle2_r18emsye')],
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


def search_manager(titles: list, movie: str, to_show: bool) -> pd.DataFrame:
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
        print('='*80)
        print(table.head())
        print('=' * 80)
    else:
        bar = FillingCirclesBar('Searching: ', max=len(THEATER_DICT.keys()) + 1)
        bar.next()
        table = pd.DataFrame(index=titles)
        for key in THEATER_DICT:
            result = [search(title, key) for title in titles]
            table[key] = result
            bar.next()
        if to_show:
            print('\n' + '=' * 80)
            print(table)
            print('=' * 80)
        bar.finish()
        print(f"Searching of {len(titles)} movies done.\nCheck results.csv")
    return table


def parse_args() -> Tuple[str, bool]:
    """
    Parsing of initial flags --single and --show
    Returns
    -------
    Tuple:
        Params to use
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--single", type=str, help='Single title to find')
    parser.add_argument("--show", type=bool, default=False, help='Showing results in CLI')
    args = parser.parse_args()
    return args.single, args.show


if __name__ == '__main__':
    # todo: Сделать обработчик состояний файлов search_list.txt и result.txt
    # todo: Переписать search_manager()
    # todo: Подумать над добавлением западных кинотеатров + поиске фильмов на английском языке
    single_movie, show = parse_args()
    movies_to_find = get_titles('search_list.txt')
    search_manager(movies_to_find, single_movie, show).to_csv('result.csv')
