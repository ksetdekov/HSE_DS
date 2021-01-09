V = int(input())


def m_to_edge(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1:
                print(i + 1, j + 1, sep=" ")
    return 0


matrix = [list(map(int, input().split())) for _ in range(V)]

m_to_edge(matrix)
