"""
3223. Minimium Length of String After Operations
"""

from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        N = len(s)
        if N < 3:
            return N

        c = Counter(s)

        ans = 0
        for v in c.values():
            if v < 3:
                ans += v
            else:
                ans += 1 + (v - 3) % 2

        return ans
