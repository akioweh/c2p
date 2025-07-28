"""
1980. Find Unique Binary String
"""


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        N = len(nums)
        nums = [int(n, 2) for n in nums]
        nums.sort()
        for i, v in enumerate(nums):
            if i != v:
                return f'{i:0{N}b}'
        return f'{N:0{N}b}'
