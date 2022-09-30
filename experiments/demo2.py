import gc
import psutil
import os


def bytesto(bytes, to, bsize=1024):
    a = {'k': 1, 'm': 2, 'g': 3, 't': 4, 'p': 5, 'e': 6 }
    r = float(bytes)
    return r / (bsize ** a[to])


class MyClass:
    def __init__(self):
        self._dict = {"0": ' ' * 128 * 1024 * 1024}
    def clear(self):
        self._dict = {}


def print_memory():
    process = psutil.Process(os.getpid())
    print(f"memory usage {bytesto(process.memory_info().rss, 'm')} M")  # in MB

def main():
    for _ in range(5):
        a = MyClass()
        a.clear()
        print_memory()


if __name__ == "__main__":
    main()
