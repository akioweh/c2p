"""
2342. Max Sum of a Pair With Equal Sum of Digits
"""

from functools import partial


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        summed = list(map(sum, map(partial(map, int), map(str, nums))))

        maxes: dict[int, tuple[int, int]] = {}
        for v, s in zip(nums, summed):
            if s not in maxes:
                maxes[s] = -1 - v, v
            else:
                l, r, = maxes[s]
                if v > r:
                    maxes[s] = r, v
                elif v > l:
                    maxes[s] = v, r

        return max(map(sum, maxes.values()))
