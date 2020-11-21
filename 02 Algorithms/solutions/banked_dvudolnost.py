import sys
from collections import defaultdict

n, m = list(map(int, input()))
graph = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

colour = [0 for i in range(n)]


def dfs(vertex, c):
    colour[vertex - 1] = True

    for col in graph[vertex]:
        if colour[u - 1] == 0:
            dfs(u - 1, (c % 2) + 1)
        elif colour[col] == c:
            print("NO")
            sys.exit(0)


ans = []
for i in range(n):
    v = i + 1
    if colour[i] == 0:
        dfs(i + 1, 1)

    if colour[i] == 1:
        ans.append(v)

print("YES")
print(*ans)
