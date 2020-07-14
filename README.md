# 1k_movie_checker
### Quick info

Bunch of parsers to check top 1000 movies in two online platforms.

List of movies was collected from https://www.kinonews.ru/top100_p1

Main module can perform search over https://www.ivi.ru/ and https://megogo.ru/

Main idea of this project was to create a python based parser which can perform search requests to server and parse results of this search

### Dependencies

`from urllib.request import urlopen as uReq, quote`

`from bs4 import BeautifulSoup as soup` 

`import pandas as pd` 

`from math import nan`

`import openpyxl`

### Getting started

To make a quick search you can simply open `search_list.txt` and put movie titles you're interested in line by line.  Then run `parser.py`.  When script is over you can check results in `result.xlsx`

