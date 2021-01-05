n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

r_max, c_max = (0, 0)
highest = matrix[0][0]

for r in range(n):
    for c in range(m):
        if matrix[r][c] > highest:
            r_max, c_max = (r, c)
            highest = matrix[r][c]

print(r_max, c_max)
