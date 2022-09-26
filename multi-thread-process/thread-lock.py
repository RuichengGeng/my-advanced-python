# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:00:33 2021

@author: Ruich
Since threads are still executed with in one process and has shared variables and resources, so some time need
a lock of some shared variables to make sure multi-thread not change one shared variable at the same time.
We can just use simple with lock statement to do it.
"""

import threading
import time

lock = threading.Lock()


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    if account.balance >= amount:
        time.sleep(0.1)
        account.balance -= amount
        print("success, balance = {}".format(account.balance))
    else:
        print("fail, balance = {}".format(account.balance))
    if account.balance > 0:
        raise ValueError("Account balance lower than 0!")


def draw_lock(account, amount):
    with lock:
        if account.balance >= amount:
            time.sleep(0.1)
            account.balance -= amount
            print("success, balance = {}".format(account.balance))
        else:
            print("fail, balance = {}".format(account.balance))


def unlock_func():
    try:
        account = Account(1000)
        amounts = [800, 600]
        threads = []
        for amount in amounts:
            threads.append(
                threading.Thread(target=draw, args=(account, amount,))
            )
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    except ValueError as e:
        print(e)


def locked_func():
    try:
        account = Account(1000)
        amounts = [800, 600]
        threads = []
        for amount in amounts:
            threads.append(
                threading.Thread(target=draw_lock, args=(account, amount,))
            )
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    except ValueError as e:
        print(e)


def main():
    unlock_func()
    locked_func()


if __name__ == '__main__':
    main()