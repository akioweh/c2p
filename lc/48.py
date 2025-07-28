"""
48. Rotate Image
"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        def swap(i1, j1, i2, j2):
            matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]

        # in-place square 2d array rotation
        N = len(matrix)
        for d in range(N // 2):
            for n in range(N - d * 2 - 1):
                swap(d, d + n, d + n, -1 - d)
                swap(d, d + n, -1 - d, -1 - d - n)
                swap(d, d + n, -1 - d - n, d)
