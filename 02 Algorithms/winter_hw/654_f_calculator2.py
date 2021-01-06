N = int(input())


def calc(n):
    if n <= 1:
        return ""
    steps = [0 for _ in range(n)]
    action = [-1 for _ in range(n)]
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
        this_action = options.index(min(options)) + 1

        action[i] = this_action

    path = []
    crawl = action[-1]  # destination
    i = n - 1
    while crawl != -1:
        path.append(crawl)
        if crawl == 1:
            i = i - 1
        elif crawl == 2:
            i = (i + 1) // 2 - 1
        else:
            i = (i + 1) // 3 - 1
        crawl = action[i]

    result = list(reversed(path))

    return ''.join(map(str, result))


print(calc(N))
