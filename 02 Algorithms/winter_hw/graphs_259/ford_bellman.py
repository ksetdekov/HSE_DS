def ford_bellman(start):
    d = [float('inf') for i in range(n)]
    d[start] = 0

    for i in range(n):
        for u, v, c in edges:
            d[v] = min(d[v], d[u] + c)
    
    return d




if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []

    for i in range(m):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))

    print(ford_bellman(0))
