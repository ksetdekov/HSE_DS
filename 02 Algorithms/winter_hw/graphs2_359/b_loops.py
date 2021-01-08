V = int(input())


def loop_test(mat):
    for i in range(len(mat)):
        if mat[i][i] == 1:
            return "YES"

    return "NO"


matrix = [list(map(int, input().split())) for _ in range(V)]

print(loop_test(matrix))
