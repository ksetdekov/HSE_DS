def ford_bellman(start):

    d = [float("Inf") for _ in range(n)]
    d[start] = 0
    """o(NM) выгодно когда n>>m список ребер берет"""
    for i in range(n):
        """o(n) """
        for u, v, c in edges:
            """o(m)"""
            d[v] = min(d[v], d[u] + c)
    return d


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []

    for i in range(m):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))

    print(ford_bellman(0))
