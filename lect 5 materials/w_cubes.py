import math

n_inp = int(input())
result = []


def c_root(k):
    """cube root calculator based on newton formula"""
    start = math.floor(len(str(k).encode('utf-8')) / 3) + 1
    x = start
    while True:
        x = (x - (x ** 3 - k) / (3 * x ** 2))//1
        if x ** 3 <= k < (x + 1) ** 3:
            break
    return x


print(c_root(n_inp))
