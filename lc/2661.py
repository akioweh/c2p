"""
2661. First Completely Painted Row or Column
"""

class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        M, N = len(mat), len(mat[0])

        idxs = {}
        for i, r in enumerate(mat):
            for j, v in enumerate(r):
                idxs[v] = i, j

        row_ns = [M] * N
        col_ns = [N] * M

        for k, v in enumerate(arr):
            r, c = idxs[v]
            row_ns[c] -= 1
            col_ns[r] -= 1
            if not row_ns[c] or not col_ns[r]:
                return k
