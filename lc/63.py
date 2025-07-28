"""
63. Unique Paths II
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = []
        blocked = False
        for v in obstacleGrid[0]:
            if v == 1:
                blocked = True
            dp.append(0 if blocked else 1)

        for i in range(1, M):
            dp[0] = 0 if obstacleGrid[i][0] else dp[0]
            for j in range(1, N):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]

        return dp[-1]
