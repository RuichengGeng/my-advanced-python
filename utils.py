
def bytesto(bytes, to, bsize=1024):
    a = {'k': 1, 'm': 2, 'g': 3, 't': 4, 'p': 5, 'e': 6 }
    r = float(bytes)
    return r / (bsize ** a[to])

