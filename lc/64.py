"""
64. Minimum Path Sum
"""

from itertools import accumulate


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = list(accumulate(grid[0]))

        for i in range(1, M):
            dp[0] += grid[i][0]
            for j in range(1, N):
                dp[j] = grid[i][j] + min(dp[j], dp[j - 1])

        return dp[-1]
