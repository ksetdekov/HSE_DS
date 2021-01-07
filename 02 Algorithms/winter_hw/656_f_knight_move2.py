N, M = map(int, input().split())

matrix = [[0 for _ in range(M)] for _ in range(N)]


def find_diagonal_order(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[int]
    """
    d = {}
    # loop through matrix
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            # if no entry in dictionary for sum of indices aka the diagonal, create one
            if i + j not in d:
                d[i + j] = [(i, j)]
            else:
                # If you've already passed over this diagonal, keep adding elements to it!
                d[i + j].append((i, j))
        # we're done with the pass, let's build our answer array
    ans = []
    # look at the diagonal and each diagonal's elements
    for entry in d.items():
        # each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
        # snake time, look at the diagonal level
        if entry[0] % 2 == 0:
            # Here we append in reverse order because its an even numbered level/diagonal.
            [ans.append(x) for x in entry[1][::-1]]
        else:
            [ans.append(x) for x in entry[1]]
    return ans


def knight_moves(rows, columns, order):
    for elem in order:
        i = elem[0]
        j = elem[1]
        matrix[i][j] = matrix[i - 2][j - 1] + matrix[i - 2][j + 1] + matrix[i - 1][j - 2] + matrix[i + 1][j - 2]

    return matrix[rows][columns]


look_seq = find_diagonal_order(matrix)

matrix = [[0 for _ in range(M + 2)] for _ in range(N + 2)]

matrix[0][0] = 1

print(knight_moves(N - 1, M - 1, look_seq[1:]))
