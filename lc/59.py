"""
59. Spiral Matrix II
"""


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [
            [-1] * n
            for _ in range(n)
        ]

        dirl = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        )

        v_lo = 1
        for layer in range(n // 2):
            this_n = n - layer * 2
            v_hi = v_lo + 4 * (this_n - 1)
            i, j = layer, layer
            for v in range(v_lo, v_hi):
                matrix[i][j] = v
                di, dj = dirl[(v - v_lo) // (this_n - 1)]
                i, j = i + di, j + dj
            v_lo = v_hi

        if n % 2:
            matrix[n // 2][n // 2] = n * n

        return matrix
