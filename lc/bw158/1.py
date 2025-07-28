from itertools import groupby


class Solution:
    def maxSumDistinctTriplet(self, x: list[int], y: list[int]) -> int:
        tmp = list(range(len(x)))
        tmp.sort(key=x.__getitem__)
        new_y = []
        for vi, vs in groupby(tmp, key=x.__getitem__):
            new_y.append(max(y[i] for i in vs))

        if len(new_y) < 3:
            return -1
        return sum(sorted(new_y, reverse=True)[:3])
