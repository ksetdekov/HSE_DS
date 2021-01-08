V = int(input())

matrix = [list(map(int, input().split())) for _ in range(V)]


def loop3_find(mat):
    len_max = float("Inf")
    best = ()
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            for k in range(len(mat)):
                if i < j < k:
                    length = mat[i][j] + mat[j][k] + mat[k][i]
                    if length < len_max:
                        len_max = length
                        best = [i + 1, j + 1, k + 1]
    return " ".join(map(str, best))


print(loop3_find(matrix))
