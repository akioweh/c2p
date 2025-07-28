"""
73. Set Matrix Zeroes
"""

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = []
        cols = []
        for i, r in enumerate(matrix):
            for j, c in enumerate(r):
                if c == 0:
                    rows.append(i)
                    cols.append(j)

        for i in rows:
            matrix[i][:] = [0] * len(matrix[i])
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0

