V = int(input())


def e_count(mat):
    edges = 0
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            if mat[i][j] == 1:
                edges += 1

    return edges


matrix = [list(map(int, input().split())) for _ in range(V)]

print(e_count(matrix))
