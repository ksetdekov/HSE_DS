def phib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return phib(n - 2) + phib(n - 1)


a = int(input())
print(phib(a))
