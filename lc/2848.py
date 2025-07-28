"""
2848. Points That Intersect With Cars
"""

from math import floor, ceil


class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        covered: set[int] = set()
        covered.update(*(range(ceil(start), floor(end) + 1) for start, end in nums))
        return len(covered)
