import sys

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
visited = [False for i in range(n)]

def dfs(v, prev):
    visited[v] = True

    for u in range(n):
        if graph[v][u] == 1 and u != prev:
            if not visited[u]:
                dfs(u, v)
            else:
                print("NO")
                sys.exit(0)

dfs(0, -1)
if False in visited:
    print("NO")
else:
    print("YES")