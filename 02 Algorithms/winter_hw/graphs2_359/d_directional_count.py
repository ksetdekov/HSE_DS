V = int(input())


def e_count(mat):
    edges = 0
    for i in range(len(mat)):
        edges += sum(mat[i])

    return edges


matrix = [list(map(int, input().split())) for _ in range(V)]

print(e_count(matrix))
