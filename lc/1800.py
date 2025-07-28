"""
1800. Maximum Ascending Subarray Sum
"""


class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        N = len(nums)
        cur_sum = nums[0]
        max_sum = 0
        for i in range(1, N):
            inc = nums[i] > nums[i - 1]
            eq = nums[i] == nums[i - 1]
            if eq or not inc:
                max_sum = max(max_sum, cur_sum)
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]

        return max(max_sum, cur_sum)
