N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]


def expensive(n, m, grid):
    costs = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    matrix_ans = [[[] for _ in range(m + 1)] for _ in range(n + 1)]
    for r in range(n):
        for c in range(m):
            if c == 0:
                costs[r + 1][c + 1] = costs[r][c + 1] + grid[r][c]
                matrix_ans[r + 1][c + 1] = matrix_ans[r][c + 1].copy()
                matrix_ans[r + 1][c + 1].extend('D')
            elif r == 0:
                costs[r + 1][c + 1] = costs[r + 1][c] + grid[r][c]
                matrix_ans[r + 1][c + 1] = matrix_ans[r + 1][c].copy()
                matrix_ans[r + 1][c + 1].extend('R')
            else:
                costs[r + 1][c + 1] = max(costs[r][c + 1], costs[r + 1][c]) + grid[r][c]
                if costs[r][c + 1] > costs[r + 1][c]:
                    matrix_ans[r + 1][c + 1] = matrix_ans[r][c + 1].copy()
                    matrix_ans[r + 1][c + 1].extend('D')
                else:
                    matrix_ans[r + 1][c + 1] = matrix_ans[r + 1][c].copy()
                    matrix_ans[r + 1][c + 1].extend('R')

    result = matrix_ans[-1][-1]
    result = result[1:]
    ans = " ".join(str(x) for x in result)
    print(costs[-1][-1])
    return ans


print(expensive(N, M, matrix))
