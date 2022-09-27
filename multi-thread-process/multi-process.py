# -*- coding: utf-8 -*-
"""

@author: Ruicheng

In python, the grammar of multi-process pool is nearly the same with multi-thread pool. But please note that
there are lots of methods like: map, starmap and imap... and parameters: workers, chunksize...
you can manipulate with, please google it when optimization is needed
"""
import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

PRIMES = [112272535095293] * 30000000


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return True
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n):
        if n % i == 0:
            return False
        return True


def single_process():
    for num in PRIMES:
        is_prime(num)


def multithread_process():
    with ThreadPoolExecutor() as pool:
        result = pool.map(is_prime, PRIMES)


def multiprocess_process():
    with ProcessPoolExecutor() as pool:
        result = pool.map(is_prime, PRIMES)

def main():
    start = time.time()
    single_process()
    end = time.time()
    print("Single thread {}".format(end - start))

    start = time.time()
    multithread_process()
    end = time.time()
    print("multi thread {}".format(end - start))

    # in single core pc multiprocess will not be faster
    start = time.time()
    multiprocess_process()
    end = time.time()
    print("multi process {}".format(end - start))


if __name__ == '__main__':
    main()
