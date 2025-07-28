from itertools import groupby


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for _, g in groupby(s):
            if len(list(g)) == k:
                return True
        return False
