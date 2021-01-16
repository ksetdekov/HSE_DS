N, X, Y = map(int, input().split())
topans = max(X, Y) * N


def is_answer(this_count, count, left, right):
    tmp = this_count - min(left, right)
    a = tmp // left
    b = tmp // right
    number_of = a + b + 1
    return number_of >= count


def left_binsearch_ans(n, x, y):
    l, r = 0, topans
    while r > l + 1:
        m = (r + l) // 2
        if is_answer(m, n, x, y):
            r = m
        else:
            l = m

    return r


print(left_binsearch_ans(N, X, Y))
