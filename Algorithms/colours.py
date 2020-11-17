count = int(input())
matrix = []
for i in range(count):
    matrix.append(list(map(int, input().split())))

a = input()
colours = list(map(int, input().split()))

bad = 0
for row in range(len(matrix)):
    for col in range(row, len(matrix)):
        if matrix[row][col] == 1:
            if colours[row] != colours[col]:
                bad += 1
print(bad)
