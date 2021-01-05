a = int(input())


def hard_seq(n):
    seq = [0 for _ in range(max(n + 1, 2))]
    seq[0] = 1
    seq[1] = 1
    if n < 2:
        return seq[n]

    for i in range(2, n + 1):
        ind = int(i / 2)
        if i % 2 == 0:
            seq[i] = seq[ind] + 1
        else:
            seq[i] = seq[ind] + 1 + seq[ind + 1]
    return seq[-1]


print(hard_seq(a))
