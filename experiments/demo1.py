import psutil
import os

def bytesto(bytes, to, bsize=1024):
    a = {'k': 1, 'm': 2, 'g': 3, 't': 4, 'p': 5, 'e': 6 }
    r = float(bytes)
    return r / (bsize ** a[to])


def fun():
    return ' ' * 128 * 1024 * 1024

def main():
    fun()
    process = psutil.Process(os.getpid())
    print(f"memory usage {bytesto(process.memory_info().rss, 'm')} M")  # in MB


if __name__ == '__main__':
    while True:
        main()