n1 = int(input())
p1 = list(map(int, input().split()))
n2 = int(input())
p2 = list(map(int, input().split()))

# n1 = 3
# p1 = [1, 2, 3]
# n2 = 3
# p2 = [ 2, 3, 1]


# 1) если не равны значения максимум
#
# * значение сверху
# * значение слева
# 2) если равны максимум
#
# * значение сверху
# * значение слева
# * сверху слева +1
def big_com_seq(a, b):
    la = len(a)
    lb = len(b)
    matrix = [[0 for _ in range(lb + 1)] for _ in range(la + 1)]
    matrix_ans = [[[] for _ in range(lb + 1)] for _ in range(la + 1)]
    for i in range(la):
        for j in range(lb):
            # print(i, "i", j, "j")
            # print(matrix)
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
            if matrix[i - 1][j] >= matrix[i][j - 1]:
                matrix_ans[i][j].extend(matrix_ans[i - 1][j])
            else:
                matrix_ans[i][j].extend(matrix_ans[i][j - 1])
            if a[i] == b[j]:
                if matrix[i][j] > 1 + matrix[i - 1][j - 1]:
                    matrix_ans[i][j] = matrix_ans[i][j]
                else:
                    matrix_ans[i][j] = matrix_ans[i - 1][j - 1]
                    matrix_ans[i][j].extend([a[i]])
                matrix[i][j] = max(matrix[i][j], 1 + matrix[i - 1][j - 1])

    # print(ans)
    # print(matrix)
    # print(matrix_ans)
    ans = " ".join(str(x) for x in matrix_ans[la - 1][lb - 1])
    return ans


print(big_com_seq(p1, p2))
