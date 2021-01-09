V = int(input())

inverted_adj_list = [[] for _ in range(V)]
for current in range(V):
    j = current
    read = list(map(int, input().split()))
    for elem in read:
        inverted_adj_list[elem - 1].append(j + 1)

# for r in matrix:
#     print(*r)
print(V)
for row in inverted_adj_list:
    print(" ".join(map(str, row)))
