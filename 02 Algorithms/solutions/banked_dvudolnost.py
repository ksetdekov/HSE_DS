import sys
from collections import defaultdict

n, m = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

colour = [0 for i in range(n)]


def dfs(v_inner, c):
    colour[v_inner - 1] = c

    for u_inner in graph[v_inner]:
        if colour[u_inner - 1] == 0:
            dfs(u_inner, (c % 2) + 1)

        elif colour[u_inner - 1] == c:
            print('NO')
            sys.exit(0)


ans = []
for i in range(n):
    v = i + 1
    if colour[i] == 0:
        dfs(v, 1)

    if colour[i] == 1:
        ans.append(v)

print('YES')
print(*ans)
