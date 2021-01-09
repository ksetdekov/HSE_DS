V = int(input())
matrix = [[0 for _ in range(V)] for _ in range(V)]
adjacency_list = []
for _ in range(V):
    adjacency_list.append(list(map(int, input().split())))
# print(adjacency_list)
for vertexes in range(V):
    j = vertexes
    for elem in adjacency_list[vertexes]:
        i = elem - 1
        matrix[i][j] = 1

# for r in matrix:
#     print(*r)
print(V)
for r in matrix:
    neighbours = []
    for c in range(V):
        if r[c] == 1:
            neighbours.append(c + 1)
    print(*neighbours)
