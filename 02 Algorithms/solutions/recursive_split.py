search, N = list(map(int, input().split()))
area = list(map(int, input().split()))
area = [(i + 1, area[i]) for i in range(N)]
result = 0
# print(area)


def split_find(tofind, list_to_look):
    len_inp = len(list_to_look)
    if len_inp == 0:
        return 0

    mid = len_inp // 2
    if list_to_look[mid][1] < tofind:
        return split_find(tofind, list_to_look[mid + 1:])
    elif tofind < list_to_look[mid][1] or (0 < mid and list_to_look[mid - 1][1] == tofind):
        return split_find(tofind, list_to_look[:mid])
    else:
        return list_to_look[mid][0]


print(split_find(search, area))