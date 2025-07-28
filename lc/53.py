"""
53. Maximum Subarray
"""
from itertools import accumulate
from operator import sub


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        return max(map(sub, accumulate(nums), accumulate(accumulate(nums), min, initial=0)))
