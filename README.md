# Movie cheker

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Quick info
Small parser that performs search of specified movies in several online movie theaters.Right now works with Russian 
online movie theaters.

## Dependencies



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
