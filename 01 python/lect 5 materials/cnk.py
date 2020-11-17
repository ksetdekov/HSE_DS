def c(n, k):
    if n == k:
        return 1
    elif k == 1:
        return n
    elif k == 0:
        return 1
    else:
        return c(n - 1, k - 1) + c(n - 1, k)


n_inp = int(input())
k_inp = int(input())

print(c(n_inp, k_inp))
