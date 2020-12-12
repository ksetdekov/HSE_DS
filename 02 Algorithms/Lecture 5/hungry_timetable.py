n = int(input())
time = []
for _ in range(n):
    time.append(tuple(map(int, input().split())))


def hungry_time(count, x):
    res = []

    while len(x)>0:
        sorted_by_second = sorted(x, key=lambda tup: tup[1])
        res.append(sorted_by_second[0])
        # print("end", sorted_by_second[0][1])
        prev_res = sorted_by_second[0][1]
        x = sorted_by_second[1:]
        x = [i for i in x if i[0] >= prev_res]

        # print(x)
        # print(res)

    return len(res)


print(hungry_time(n, time))
