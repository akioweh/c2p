"""
38. Count and Say
"""

from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s2 = ''
            for k, g in groupby(s):
                s2 += f'{len(list(g))}{k}'
            s = s2
        return s
