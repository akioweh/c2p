"""
567. Permutation in String
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l2 < l1:
            return False

        target_bag = Counter(s1)

        cur_bag = Counter(s2[:l1])
        if cur_bag == target_bag:
            return True
        for i in range(l1, l2):
            cur_bag[s2[i - l1]] -= 1
            cur_bag[s2[i]] += 1
            if cur_bag == target_bag:
                return True

        return False
