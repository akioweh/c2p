"""
1422. Maximum Score After Splitting a String
"""


class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        l_score = int(s[0] == '0')
        r_score = s[1:].count('1')
        max_score = l_score + r_score
        for i in range(1, N - 1):
            if s[i] == '0':
                l_score += 1
            else:
                r_score -= 1
            max_score = max(max_score, l_score + r_score)

        return max_score
