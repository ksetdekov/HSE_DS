N, M = list(map(int, input().split()))


def table_steps(rows, columns):
    row = [0 for _ in range(M + 1)]
    prev_row = [0 for _ in range(M + 1)]
    #     print(row)
    prev_row[1] = 1
    #     print(row)

    for k in range(rows):
        for i in range(columns):
            row[i + 1] = prev_row[i + 1] + row[i]
        #             print(row)
        prev_row = row
    return row[-1]


print(table_steps(N, M))
