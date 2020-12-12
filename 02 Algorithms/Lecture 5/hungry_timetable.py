n = int(input())
time = []
for _ in range(n):
    time.append(tuple(map(int, input().split())))


def hungry_time(x):
    res = []
    sorted_by_second = sorted(x, key=lambda tup: tup[1])
    prev_res = sorted_by_second[0][0]
    for elem in sorted_by_second:
        if elem[0] >= prev_res:
            res.append(elem)
            prev_res = elem[1]

    # print(sorted_by_second)
    # print(res)

    return len(res)


print(hungry_time(time))
