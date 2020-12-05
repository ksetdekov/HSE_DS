N = int(input())


def posledovatelnost(n):
    n_pos_0 = [0 for i in range(n)]
    n_pos_1 = [0 for i in range(n)]
    n_pos_0[0] = 1
    n_pos_1[0] = 1

    for i in range(1, n):
        n_pos_0[i] = n_pos_0[i - 1] + n_pos_1[i - 1]
        n_pos_1[i] = n_pos_0[i - 1]

    return n_pos_0[-1] + n_pos_1[-1]


print(posledovatelnost(N))
