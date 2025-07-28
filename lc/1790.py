"""
1790. Check if One String Swap Can Make Strings Equal
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        N1, N2 = len(s1), len(s2)
        if N1 != N2:
            return False

        ne = []
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                ne.append((c1, c2))

        L = len(ne)
        if not L:
            return True
        if L != 2:
            return False
        a, b = zip(*ne)
        return a == b[::-1]
