"""
56. Merge Intervals
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        N = len(intervals)
        if N == 1:
            return intervals

        intervals.sort()
        merged = []
        cur_start, cur_end = intervals[0]
        for this_start, this_end in intervals[1:]:
            if this_start <= cur_end:
                cur_end = max(cur_end, this_end)
            else:
                merged.append([cur_start, cur_end])
                cur_start, cur_end = this_start, this_end

        merged.append([cur_start, cur_end])
        return merged
