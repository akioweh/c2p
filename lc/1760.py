"""
1760. Minimum Limit of Balls in a Bag
"""

from math import ceil


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        nums.sort()

        l, r = 1, nums[-1]
        while l != r:
            target_max = (l + r) // 2
            possible = False
            ops_left = maxOperations
            for n in reversed(nums):
                if n <= target_max:
                    possible = True
                    break
                ops_left -= ceil(n / target_max) - 1
                if ops_left < 0:
                    break
            else:
                possible = True

            if possible:
                r = target_max
            else:
                l = target_max + 1

        return l
