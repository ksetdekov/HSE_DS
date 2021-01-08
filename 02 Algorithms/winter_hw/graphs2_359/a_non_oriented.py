V = int(input())

matrix = [list(map(int, input().split())) for _ in range(V)]


def orietn_test(mat):

    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                if mat[i][j] == 1:
                    return "NO"
            if mat[i][j] != mat[j][i]:
                return "NO"
    return "YES"


print(orietn_test(matrix))
