A_len, B_len = map(int, input().split())
a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))


def binsearch(arr, num):
    l, r = 0, len(arr)
    if arr[0] > num:
        return "NO"
    if arr[-1] < num:
        return "NO"

    while r > l + 1:
        m = (l + r) // 2
        if arr[m] <= num:
            l = m
        else:
            r = m
    if arr[l] == num:
        return "YES"
    return "NO"


for elem_b in b_array:
    print(binsearch(a_array, elem_b))
