search, N = list(map(int, input().split()))
area = list(map(int, input().split()))


# print(area)


def binarySearch(arr, x):
    """Returns the lowest index of the element equal to `x` or NaN if not found."""
    if len(arr) == 0:
        return 0
    m = len(arr) // 2
    if arr[m] < x:
        return m + 1 + binarySearch(arr[m + 1:], x)
    elif x < arr[m] or (0 < m and arr[m - 1] == x):
        return binarySearch(arr[:m], x)
    else:
        return m


def wrapper(arr, x):
    res = binarySearch(arr, x) + 1
    if res > len(arr):
        return 0
    else:
        return res


print(wrapper(area, search))
