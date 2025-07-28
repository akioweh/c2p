"""
75. Sort Colors
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zs = 0
        os = 0
        ts = 0
        for n in nums:
            if n == 0:
                zs += 1
            elif n == 1:
                os += 1
            else:
                ts += 1
        nums[:] = [0] * zs + [1] * os + [2] * ts
