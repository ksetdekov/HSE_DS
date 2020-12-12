n1 = int(input())
p1 = list(map(int, input().split()))
n2 = int(input())
p2 = list(map(int, input().split()))


# 1) если не равны значения максимум
#
# * значение сверху
# * значение слева
# 2) если равны максимум
#
# * значение сверху
# * значение слева
# * сверху слева +1
def big_com_seq(a, b, la, lb):
    matrix = [[0 for _ in range(lb + 1)] for _ in range(la + 1)]
    for i in range(la):
        for j in range(lb):
            # print(i, "i", j, "j")
            # print(matrix)
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
            if a[i] == b[j]:
                matrix[i][j] = max(matrix[i][j], 1 + matrix[i - 1][j - 1])

    return matrix[la - 1][lb - 1]


print(big_com_seq(p1, p2, n1, n2))
