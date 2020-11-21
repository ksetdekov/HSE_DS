N, S = list(map(int, input().split()))
matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))

S -= 1

from collections import defaultdict


def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != 0:
                adjList[i].append(j)
    return adjList


graph = convert(matrix)

visited = [False for i in range(N)]


def dfs(v):
    visited[v] = True
    counter = 1
    for u in graph[v]:
        if not visited[u]:
            counter += dfs(u)
    return counter


counter = dfs(S)
print(counter)
