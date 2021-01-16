w, h, n = map(int, input().split())
topans = max(w, h) * n

def is_answer(size, width, height, count):
    down = size // height
    right = size // width
    number_of = down * right
    return number_of >= count


def left_binsearch_ans(w, h, n):
    l, r = 0, topans - 1
    while r > l + 1:
        m = (r + l) // 2
        if is_answer(m, w, h, n):
            r = m
        else:
            l = m

    return r

print(left_binsearch_ans(w, h, n))