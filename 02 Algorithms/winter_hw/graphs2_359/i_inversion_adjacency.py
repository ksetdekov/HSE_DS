V = int(input())
matrix = [[0 for _ in range(V)] for _ in range(V)]
adjacency_list = []
for _ in range(V):
    adjacency_list.append(list(map(int, input().split())))
# print(adjacency_list)
inverted_adj_list = [[] for _ in range(V)]
for current in range(V):
    j = current
    for elem in adjacency_list[current]:
        inverted_adj_list[elem - 1].append(j + 1)

# for r in matrix:
#     print(*r)
print(V)
for row in inverted_adj_list:
    print(*row)