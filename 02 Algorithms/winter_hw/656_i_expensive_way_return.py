N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]


def expensive(n, m, grid):
    costs = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    matrix_ans = [[[] for _ in range(m + 1)] for _ in range(n + 1)]
    for r in range(n):
        for c in range(m):
            if c == 0:
                costs[r + 1][c + 1] = costs[r][c + 1] + grid[r][c]
            elif r == 0:
                costs[r + 1][c + 1] = costs[r + 1][c] + grid[r][c]
            else:
                costs[r + 1][c + 1] = max(costs[r][c + 1], costs[r + 1][c]) + grid[r][c]

    ans = " ".join(str(x) for x in matrix_ans[-1][-1])
    return ans


print(expensive(N, M, matrix))
