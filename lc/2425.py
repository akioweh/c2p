"""
2425. Bitwise XOR of All Pairings
"""

from operator import xor
from functools import reduce


class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        l1_odd, l2_odd = l1 % 2, l2 % 2
        if not l1_odd and not l2_odd:
            return 0
        elif l1_odd and l2_odd:
            return reduce(xor, nums1) ^ reduce(xor, nums2)
        elif l1_odd:
            return reduce(xor, nums2)
        else:
            return reduce(xor, nums1)
