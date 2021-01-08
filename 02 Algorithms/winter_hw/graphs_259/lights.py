N, M = list(map(int, input().split()))
edges = []

for i in range(M):
    v_from, v_to = list(map(int, input().split()))
    edges.append((v_from, v_to))


def get_neighbours(v, edge_holder):
    lights = 0
    for edge in edge_holder:
        if edge[0] == v or edge[1] == v:
            lights += 1
    return lights


results = []
for i in range(N):
    results.append(get_neighbours(i + 1, edges))
print(*results)
