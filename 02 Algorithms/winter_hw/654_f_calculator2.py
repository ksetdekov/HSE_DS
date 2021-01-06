from random import randrange

N = int(input())


def calc(n):
    if n <= 1:
        return ""
    steps = [0 for _ in range(n)]
    action = [(-1, -1) for _ in range(n)]
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
        if this_action == 1:
            prev = i - 1
        elif this_action == 2:
            prev = (i + 1) // 2 - 1
        else:
            prev = (i + 1) // 3 - 1
        action[i] = (this_action, prev)
    # print(action)
    # print(steps)
    path = []
    crawl = action[-1]  # destination
    while crawl[1] != -1:
        # print(crawl[1])
        path.append(crawl[0])
        crawl = action[crawl[1]]

    result = list(reversed(path))

    return ''.join(map(str, result))


print(calc(N))

for _ in range(1000000):
    r = randrange(1000000)
    print(r, 'result', calc(r))
