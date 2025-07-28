"""
3151. Special Array I
"""


class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        N = len(nums)
        if N <= 1:
            return True

        nums1 = iter(nums)
        next(nums1)
        return all(c % 2 != p % 2 for c, p in zip(nums, nums1))
