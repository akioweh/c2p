"""
62. Unique Paths
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n > m:
            m, n = n, m

        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[-1]
