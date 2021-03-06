N = int(input())


def calc(n):
    steps = [0 for _ in range(n)]
    steps[0] = 0
    for i in range(1, n):
        value = i + 1
        variant = steps[i - 1] + 1
        a, b, c = (variant, variant, variant)
        if value % 3 == 0:
            a = steps[(value // 3 - 1)] + 1
        if value % 2 == 0:
            b = steps[(value // 2 - 1)] + 1
        steps[i] = min(a, b, c)

    return steps[-1]


print(calc(N))
