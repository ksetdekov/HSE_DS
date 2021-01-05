N = int(input())


def seq_3(n):
    if n < 3:
        return n * 2

    n -= 1

    n_pos_00 = [0 for _ in range(n)]
    n_pos_01 = [0 for _ in range(n)]
    n_pos_10 = [0 for _ in range(n)]
    n_pos_11 = [0 for _ in range(n)]

    n_pos_00[0] = 1
    n_pos_01[0] = 1
    n_pos_10[0] = 1
    n_pos_11[0] = 1

    for i in range(1, n):
        n_pos_00[i] = n_pos_00[i - 1] + n_pos_10[i - 1]
        n_pos_01[i] = n_pos_00[i - 1] + n_pos_10[i - 1]
        n_pos_10[i] = n_pos_01[i - 1] + n_pos_11[i - 1]
        n_pos_11[i] = n_pos_01[i - 1]

    return n_pos_00[-1] + n_pos_01[-1] + n_pos_10[-1] + n_pos_11[-1]


print(seq_3(N))
