"""
3066. Minimum Operations to Exceed Threshold Value II
"""

from heapq import heapify, heappop, heappush


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapify(nums)
        ops = 0
        while True:
            if nums[0] >= k:
                return ops
            a = heappop(nums)
            b = heappop(nums)
            if a > b:
                a, b = b, a
            heappush(nums, 2 * a + b)
            ops += 1
