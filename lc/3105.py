"""
3105. Longest Strictly Increasing or Strictly Decreasing Subarray
"""


class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        it = iter(nums)
        next(it)
        increasing = True
        cur_streak = 1
        max_streak = 1
        for c, n in zip(nums, it):
            inc = n > c
            if n == c or inc != increasing:
                increasing = not increasing
                max_streak = max(max_streak, cur_streak)
                cur_streak = 2 if n != c else 1
            else:
                cur_streak += 1

        return max(max_streak, cur_streak)
