count = int(input())
matrix = []
for i in range(count):
    matrix.append(list(map(int, input().split())))

# matrix = [list(map(int, input().split())) for i in range(n)]
roads = 0
for row in range(len(matrix)):
    for col in range(row, len(matrix)):
        roads += matrix[row][col]
print(roads)
