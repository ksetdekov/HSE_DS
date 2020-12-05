value = int(input())


def dumb_fib(n):
    if n < 3:
        return 1
    else:
        return dumb_fib(n - 1) + dumb_fib(n - 2)


print(dumb_fib(value + 1))
