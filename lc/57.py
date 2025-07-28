"""
57. Insert Interval
"""

from bisect import bisect_left, bisect_right
from operator import itemgetter


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # index of leftmost interval who *ends* at or after new*Start*
        idx_a = bisect_left(intervals, newInterval[0], key=itemgetter(1))
        # index of leftmost interval who *starts* after new*End*
        idx_b = bisect_right(intervals, newInterval[1], key=itemgetter(0))

        # i.e. intervals[idx_b] is the first interval fully after newInterval (0 overlap);
        # intervals[idx_a - 1] is the last interval fully before newInterval.

        # so, if (idx_b) and (idx_a - 1) is exactly 1 apart,
        # we know that newInterval fits exactly between two existing intervals with 0 overlap
        if idx_a == idx_b:
            intervals.insert(idx_b, newInterval)
            return intervals

        # otherwise, newInterval overlaps with 1 or more existing intervals
        # the *first* interval that it overlaps with is at idx_a;
        # the *last* interval that it overlaps with is at idx_b - 1...
        # so we take the min/max bounds w.r.t. them.
        # Note that we do not care about any intervals between idx_a and idx_b - 1
        # because they will be fully englufed by newInterval and have to be merged.
        merged = [[
            min(intervals[idx_a][0], newInterval[0]),
            max(intervals[idx_b - 1][1], newInterval[1])
        ]]
        return intervals[:idx_a] + merged + intervals[idx_b:]
