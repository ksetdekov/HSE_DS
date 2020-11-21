import sys
from collections import deque


def get_path(v, prev):
    ans = []
    while v != -1:
        ans.append(v + 1)
        v = prev[v]
    return ans[::-1]


n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
visited = [False for i in range(n)]

start, finish = map(int, input().split())

start -= 1
finish -= 1
Q = deque()
previous = dict()

Q.append((start, 0))
visited[start] = True
previous[start] = -1

while len(Q) != 0:
    v, length = Q.popleft()

    if v == finish:
        print(length)
        print(*get_path(v, previous))
        sys.exit(0)

    for u in range(n):
        if graph[v][u] == 1 and not visited[u]:
            visited[u] = True
            Q.append((u, length + 1))
            previous[u] = v
