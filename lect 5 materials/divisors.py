value = int(input())


def MinDivisor(n):
    lim = int(n ** 0.5)

    for i in range(2, lim + 1):
        if n % i == 0:
            return i
    return n


print(MinDivisor(value))
