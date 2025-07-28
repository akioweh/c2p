"""
76. Minimum Window Substring
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        M, N = len(s), len(t)
        target_bag = Counter(t)

        cur_bag = Counter(s[:N])
        min_len = M + 1
        min_idx = (0, 0)
        l, r = 0, N
        while l <= M - N:
            if cur_bag >= target_bag:
                if r - l < min_len:
                    min_len = r - l
                    min_idx = (l, r)
                cur_bag[s[l]] -= 1
                l += 1
                continue
            elif r >= M:
                break
            cur_bag[s[r]] += 1
            r += 1

        return s[min_idx[0]:min_idx[1]]
