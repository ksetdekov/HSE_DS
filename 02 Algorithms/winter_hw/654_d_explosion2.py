N = int(input())


def explosion_3(n):
    n_pos_B = [0 for i in range(n)]
    n_pos_A = [0 for i in range(n)]
    n_pos_C = [0 for i in range(n)]
    n_pos_B[0] = 1
    n_pos_A[0] = 1
    n_pos_C[0] = 1

    for i in range(1, n):
        n_pos_C[i] = n_pos_C[i - 1] + n_pos_B[i - 1] + n_pos_A[i - 1]
        n_pos_B[i] = n_pos_C[i - 1] + n_pos_B[i - 1] + n_pos_A[i - 1]
        n_pos_A[i] = n_pos_C[i - 1] + n_pos_B[i - 1]

    return n_pos_B[-1] + n_pos_A[-1] + n_pos_C[-1]


print(explosion_3(N))
