# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:

    def longestPalindrome(self, s: str):
        a = s
        b = s[::-1]
        la = len(a)
        lb = len(b)
        if len(s) == 0:
            return ""
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
        ans = "".join(matrix_ans[la - 1][lb - 1])
        return ans
