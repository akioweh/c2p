"""
55. Jump Game
"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        N = len(nums)
        if N == 1:
            return True

        max_reach = 0
        for i, r in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, r + i)

        return max_reach >= N - 1
