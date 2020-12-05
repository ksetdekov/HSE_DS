value = int(input())


def fib(n):
    fib_number = [0 for _ in range(n)]
    fib_number[0] = 1
    fib_number[1] = 1

    for i in range(2, n):
        fib_number[i] = fib_number[i - 1] + fib_number[i - 2]
    return fib_number[-1]


print(fib(value + 1))
