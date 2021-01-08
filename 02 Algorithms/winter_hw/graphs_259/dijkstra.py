from heapq import heappop, heappush


def dijkstra(start):
    heap = []
    dist = [float('inf') for i in range(n)]

    heappush(heap, (0, start))
    dist[start] = 0

    while len(heap) > 0:
        d, v = heappop(heap)
        if dist[v] < d:
            continue

        for u, c in graph[v]:
            if d + c < dist[u]:
                dist[u] = d + c
                heappush(heap, (dist[u], u))

    return dist


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for j in range(n)]

    for i in range(m):
        v, u, c = map(int, input().split())
        graph[v].append((u, c))
        graph[u].append((v, c))

    print(dijkstra(0))
