N = int(input())


def calc(n):
    steps = [-1 for _ in range(n)]
    action = [0 for _ in range(n)]
    steps[0] = 0
    for i in range(1, n):
        value = i + 1
        variant = steps[i - 1] + 1
        a, b, c = (variant, variant, variant)
        if value % 3 == 0:
            a = steps[(value // 3 - 1)] + 1
        if value % 2 == 0:
            b = steps[(value // 2 - 1)] + 1
        options = [c, b, a]
        steps[i] = min(options)
        action[i] = options.index(min(options)) + 1
    print(action)
    path = []
    crawl = action[-1]  # destination
    path.append(crawl)
    while (action[crawl - 1] != -1):

        path.append(action[crawl - 1])
        crawl = action[crawl - 1]

    print(list(reversed(path)))

    return steps[-1]


print(calc(N))


