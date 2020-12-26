def floyd_warshall(start):
    d = [float("Inf") for i in range(n)]
    dist = [[graph[j][i] for i in range(n)] for j in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[j][k] + dist[k][j])
    return dist

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[float("Inf") for i in range (n)] for j in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for i in range(m):
        u, v, c = map(int, input().split())
        graph[u][v] = c
    # for line in floyd_warshall(0):
        