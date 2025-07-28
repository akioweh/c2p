"""
91. Decode Ways
"""

from functools import cache


class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 1
        if N == 1:
            return 1 if s != '0' else 0

        s0 = int(s[0])
        s1 = int(s[1])
        if s0 >= 3:  # only 1 choice
            return self.numDecodings(s[1:])
        elif s0 == 2:
            tmp = self.numDecodings(s[1:])
            if s1 <= 6:
                tmp += self.numDecodings(s[2:])
            return tmp
        elif s0 == 1:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        else:  # s0 == 0; impossible
            return 0
