def binsearch(arr, num):
    l, r = 0, len(arr)

    while r > l + 1 :
        m = (l + r) // 2

        if arr[m] < num:
            l = m
        else:
            r = m
        
    return   