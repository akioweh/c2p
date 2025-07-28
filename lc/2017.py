"""
2017. Grid Game
"""

from itertools import accumulate


class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        N = len(grid[0])

        pfs_r1 = list(accumulate(grid[0]))  # prefix sum of row 1
        pfs_r2 = list(accumulate(grid[1]))  # ...of row 2
        sum_r1 = pfs_r1[-1]
        sum_r2 = pfs_r2[-1]
        pfs_r2.append(0)  # avoid out of bounds at line 21

        min_max = sum_r1 + sum_r2  # guaranteeded "large enough" number
        for corner_c in range(N):  # "turning column" of robot 1
            opt1 = sum_r1 - pfs_r1[corner_c]  # if robot 2 collects all in top row
            opt2 = pfs_r2[corner_c - 1]  # if robot 2 collects all in bottom row
            min_max = min(min_max, max(opt1, opt2))  # minimax

        return min_max
