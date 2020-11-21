from collections import defaultdict

n, m = list(map(int, input().split()))

graph = defaultdict(list)
for i in range(m):
    v_from, v_to = list(map(int, input().split()))
    graph[v_from].append(v_to)
    graph[v_to].append(v_from)

visited = [0 for i in range(n)]
order = 0


def dfs(v, colour):
    visited[v - 1] = colour
    for u in graph[v]:
        if not visited[u - 1]:
            dfs(u, colour)


counter = 0

for k in range(n):
    if visited[k] == 0:
        counter += 1
        order += 1
        dfs(k + 1, order)

print(order)
for col in range(1, order + 1):
    elements = [i + 1 for i, x in enumerate(visited) if x == col]
    print(len(elements))
    print(*elements)
