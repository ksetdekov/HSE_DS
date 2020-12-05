N, M = list(map(int, input().split()))
# N, M = (2, 3)


def simple_add(n, m):
    if m == 0:
        return n
    elif m > 0:
        return simple_add(n + m, 0)
    else:
        return simple_add(n + m, 0)


print(simple_add(N, M))
