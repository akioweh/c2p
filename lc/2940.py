"""
2940. Find Building Where Alice and Bob Can Meet
"""


from bisect import bisect_left


class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        N = len(heights)
        M = len(queries)
        ans = [-1] * M

        heights_idx = list(range(N))
        # sort [idx] so heights[idx] is ascending
        heights_idx.sort(key=heights.__getitem__)

        for i, (a, b) in enumerate(queries):
            if a > b:  # ensure b > a
                a, b = b, a

            if a == b or heights[a] < heights[b]:
                ans[i] = b
                continue

            min_height = heights[a] + 1  # minimum height at which a and b can meet
            # idx to start linear search (heights[heights_idx[idx]] >= min_height for all idx >= j )
            j = bisect_left(heights_idx, min_height, key=heights.__getitem__)
            if j == N:  # no heights are greater than or equal to min_height
                continue

            # search for smallest idx | heights_idx[idx] > a
            ans[i] = min(
                (heights_idx[idx]
                 for idx in range(j, N)
                 if heights_idx[idx] > b),
                default=-1
            )

        return ans
