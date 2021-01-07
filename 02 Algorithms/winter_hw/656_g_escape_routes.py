N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]


def n_routes(n, m, grid):
    routes = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    routes[0][1] = 1
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                routes[r + 1][c + 1] = routes[r][c + 1] + routes[r + 1][c]
            else:
                routes[r + 1][c + 1] = 0

    if routes[-1][-1] == 0:
        return "Impossible"
    return routes[-1][-1]


print(n_routes(N, M, matrix))
