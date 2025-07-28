"""
1752. Check if Array Is Sorted and Rotated
"""

from operator import lt


class Solution:
    def check(self, nums: list[int]) -> bool:
        non_increasing = map(lt, nums[1:], nums)
        s = sum(non_increasing)
        return s == 0 or s == 1 and nums[0] >= nums[-1]
