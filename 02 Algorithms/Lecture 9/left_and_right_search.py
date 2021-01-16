A_len, B_len = map(int, input().split())
a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))


def binsearch(arr, num):
    l, r = 0, len(arr)
    if arr[0] > num:
        return 0
    if arr[-1] < num:
        return 0

    while r > l + 1:
        m = (l + r) // 2
        if arr[m] <= num:
            l = m
        else:
            r = m
    if arr[l] == num:
        return l+1
    return r+1


def left_binsearch(arr, num):
    # l - ссылается гарантированно меньше, r - на тот, который больше или равно
    l, r = -1, len(arr) - 1
    if arr[r] < num:
        return 0

    while r > l + 1:
        m = (r + l) // 2

        if arr[m] < num:
            l = m
        else:
            r = m

    if arr[r] == num:
        return r+1
    return 0


for elem_b in b_array:
    right_res = binsearch(a_array, elem_b)
    left_res  = left_binsearch(a_array, elem_b)
    if right_res == 0:
        print(0)
        continue
    print(left_res, right_res , sep=" ")
