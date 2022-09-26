# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:18:44 2021

@author: Ruicheng

Thread pool is just easy to use and easy to control input/output in my mind... Just get familiar how thread pool
is called is enough...
"""
import time
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests


def craw(url):
    r = requests.get(url)
    return r.text


def ten_workers():
    # Please note that there are lots of parameters about thread pool executor, can take a look if optimization is needed
    urls = [
        f"https://www.cnblogs.com/#p{page}"
        for page in range(1, 51)
    ]
    with ThreadPoolExecutor(max_workers=10) as pool:
        htmls = pool.map(craw, urls)
    for idx, html in enumerate(htmls):
        print(urls[idx], len(html))


def twenty_workers():
    # Please note that there are lots of parameters about thread pool executor, can take a look if optimization is needed
    urls = [
        f"https://www.cnblogs.com/#p{page}"
        for page in range(51, 101)
    ]
    with ThreadPoolExecutor(max_workers=20) as pool:
        htmls = pool.map(craw, urls)
    for idx, html in enumerate(htmls):
        print(urls[idx], len(html))


def main():
    # here you can see 20 workers are faster than 10 
    start = time.time()
    ten_workers()
    end = time.time()
    print("10 worker thread {}".format(end - start))

    start = time.time()
    twenty_workers()
    end = time.time()
    print("20 worker thread {}".format(end - start))



if __name__ == "__main__":
    main()


