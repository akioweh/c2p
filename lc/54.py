"""
54. Spiral Matrix
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        if N == 0:
            return []
        if M == 1:
            return matrix[0]
        if N == 1:
            return [row[0] for row in matrix]

        res = []
        res.extend(matrix[0])
        res.extend(r[-1] for r in matrix[1:])
        res.extend(matrix[-1][-2::-1])
        res.extend(r[0] for r in matrix[-2:0:-1])

        return res + self.spiralOrder([r[1:-1] for r in matrix[1:-1]])
