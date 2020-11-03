# Movie checker

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 

![GitHub Releases](https://img.shields.io/github/downloads/mvrck96/1k_movie_checker/0.1/total?logo=release&style=flat-square) ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/mvrck96/1k_movie_checker)


## Quick info
Small parser that performs search of specified movies in several online movie theaters. Right now works with Russian 
online movie theaters only.

## Required modules

- `pandas`
- `bs4`
- `progress`

For versions you can check `requirements.txt`



## Getting started

There two ways for using this script. First is standard one - you put picked titles to
`search_list.txt` and then run  `movie_cheker.py`. After searching process is done results can be found in `result.csv`
For that kind of run you have on flag - `--show` 
if it is set to `True` it means that result table will be printed in CLI. Second option is to use
single title search it is much faster. To perform it you need to put `--single` flag and specify the title.
You can check out examples section for additional instructions.

## Examples

Usage of `--single` flag:

```shell script
$ python movie_checker.py --single RED
================================================================================
     megogo   okko  tnt_premier  tvigle   wink
RED    True  False        False   False  False
================================================================================
```

Usage of `--show` flag:

```shell script
$ python movie_checker.py --show True
Searching:  ◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉ 100%
================================================================================
                 megogo   okko  tnt_premier  tvigle   wink
Властелин колец   False  False        False   False  False
Шерлок Холмс       True   True        False   False   True
Трейнспоттинг     False  False        False   False  False
================================================================================

Searching of 3 movies done.
Check results.csv
```

### Help

```shell script
usage: movie_checker.py [-h] [-si SINGLE] [-sh SHOW]

optional arguments:
  -h, --help            show this help message and exit
  -si SINGLE, --single SINGLE
                        Enter single movie title to perform a quick search
  -sh SHOW, --show SHOW
                        Show or not search results in terminal. False by
                        default

```
