"""
44. Wildcard Matching
"""

from operator import ior
from functools import reduce


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # lowercase characters match as-is
        # '?' matches any single character
        # '*' matches any sequence of characters

        S, P = len(s), len(p)

        prev = 1  # using integer as bitset
        for m in p:
            if m == '*':
                if prev == 0:
                    continue
                # find least significant 1 bit
                lsb = (prev & -prev).bit_length() - 1
                prev |= ((1 << S - lsb + 1) - 1) << lsb
            elif m == '?':
                prev <<= 1
            else:
                match = reduce(ior, (1 << i for i, c in enumerate(s) if c == m), 0)
                prev = (prev & match) << 1

        return bool(prev & 1 << S)
