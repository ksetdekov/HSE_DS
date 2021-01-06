N, M = map(int, input().split())

matrix = [[-1 for _ in range(M)] for _ in range(N)]
#
#
# def find_diagonal_order(mat):
#     """
#     :type mat: List[List[int]]
#     :rtype: List[int]
#     """
#     d = {}
#     # loop through matrix
#     for i in range(len(mat)):
#         for j in range(len(mat[i])):
#             # if no entry in dictionary for sum of indices aka the diagonal, create one
#             if i + j not in d:
#                 d[i + j] = [mat[i][j]]
#             else:
#                 # If you've already passed over this diagonal, keep adding elements to it!
#                 d[i + j].append(mat[i][j])
#         # we're done with the pass, let's build our answer array
#     ans = []
#     # look at the diagonal and each diagonal's elements
#     for entry in d.items():
#         # each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
#         # snake time, look at the diagonal level
#         if entry[0] % 2 == 0:
#             # Here we append in reverse order because its an even numbered level/diagonal.
#             [ans.append(x) for x in entry[1][::-1]]
#         else:
#             [ans.append(x) for x in entry[1]]
#     print(d)
#     return ans
#
#
# print(find_diagonal_order(matrix))
#
# print(matrix)

matrix[0][0] = 1


def knight_moves(rows, columns):
    if 0 <= rows < N and 0 <= columns < M:
        if matrix[rows][columns] == -1:
            matrix[rows][columns] = knight_moves(rows - 2, columns - 1) + knight_moves(rows - 2, columns + 1) + \
                                    knight_moves(rows - 1, columns - 2) + knight_moves(rows + 1, columns - 2)
    else:
        return 0
    # print(matrix)
    return matrix[rows][columns]


print(knight_moves(N - 1, M - 1))

# todo create a dictionary of all positions in diagonal order
# todo loop over them in dinamic programming way
