N = int(input())


def pascal(rows):
    if rows == 0:
        print("")
        return None
    row = [0 for _ in range(rows + 1)]
    prev_row = [0 for _ in range(rows + 1)]
    prev_row[1] = 1

    for k in range(rows):
        output = prev_row[1:]
        print(" ".join(map(str, [i for i in output if i > 0])))
        for i in range(1, rows + 1):
            row[i] = prev_row[i] + prev_row[i - 1]

        prev_row = row.copy()


pascal(N)
