A_len, B_len = map(int, input().split())
a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))


def binsearch(arr, num):
    l, r = 0, len(arr) - 1
    if arr[l] >= num:
        return arr[l]

    while r > l + 1:
        m = (l + r) // 2

        if arr[m] <= num:
            l = m
        else:
            r = m

    if abs(arr[l] - num) <= abs(arr[r] - num):
        return arr[l]

    return arr[r]


for elem_b in b_array:
    print(binsearch(a_array, elem_b))