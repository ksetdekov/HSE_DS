V, E = map(int, input().split())
matrix = [[0 for _ in range(V)] for _ in range(V)]
e_list = []
for _ in range(E):
    e_list.append(list(map(int, input().split())))

for elem in e_list:
    i = elem[0] - 1
    j = elem[1] - 1
    matrix[i][j] = 1

for r in matrix:
    print(*r)
