"""
97. Interleaving String
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N1, N2, N3 = len(s1), len(s2), len(s3)
        if N1 + N2 != N3:
            return False

        dp = [
            [False] * (N2 + 1)
            for _ in range(N1 + 1)
        ]
        #  dp[i][j] is whether s3[:i + j] is a interleaving of s1[:i] and s2[:j]

        dp[0][0] = True
        for n in range(1, N3 + 1):
            cur = s3[n - 1]
            for i in range(min(n, N1) + 1):
                j = n - i
                if j > N2:
                    continue
                s1_match = 1 <= i and s1[i - 1] == cur
                s2_match = 1 <= j and s2[j - 1] == cur
                dp[i][j] = s1_match and dp[i - 1][j] or s2_match and dp[i][j - 1]

        return dp[N1][N2]
