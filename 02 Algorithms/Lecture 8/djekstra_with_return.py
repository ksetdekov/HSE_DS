from heapq import heappop, heappush


def dijkstra(start):
    heap = []
    distances = [float('inf') for _ in range(n)]
    prev = [-1 for _ in range(n)]
    used = [False for _ in range(n)]

    heappush(heap, (0, start))
    distances[start] = 0

    while len(heap) > 0:
        d, v = heappop(heap)
        if distances[v] < d or used[v]:
            continue

        used[v] = True

        for u in range(n):
            c = graph[v][u]
            if c > 0:
                if d + c < distances[u]:
                    distances[u] = d + c
                    prev[u] = v
                    heappush(heap, (distances[u], u))

    return prev


if __name__ == "__main__":
    n, s, f = map(int, input().split())
    graph = [list(map(int, input().split())) for i in range(n)]

    prev = dijkstra(s - 1)
    # print(prev)
    if prev[f-1] == - 1 and f != s:
        print(-1)
    else:
        path = []
        v = f-1
        while v != -1:
            path.append(v+1)
            v = prev[v]

        print(*path[::-1])
