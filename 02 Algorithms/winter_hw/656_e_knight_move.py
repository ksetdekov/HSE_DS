N, M = map(int, input().split())


def knight_moves(rows, columns):
    row = [0 for _ in range(columns + 2)]
    prev_row = [0 for _ in range(columns + 2)]
    prev_prev_row = [0 for _ in range(columns + 2)]
    #     print(row)
    prev_prev_row[1] = 1

    for k in range(rows):
        for i in range(columns):
            row[i + 2] = prev_row[i] + prev_prev_row[i + 1]
        # print(row)
        prev_prev_row = prev_row.copy()

        prev_row = row.copy()

    return row[-1]


print(knight_moves(N, M))
