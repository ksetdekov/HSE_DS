value = int(input())


def min_divisor(n):
    lim = int(n ** 0.5)

    for i in range(2, lim + 1):
        if n % i == 0:
            return i
    return n


def IsPrime(n):
    return n == min_divisor(n)


if IsPrime(value):
    print('YES')
else:
    print('NO')
