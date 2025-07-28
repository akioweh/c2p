"""
407. Trapping Rain Water II
"""

from heapq import heappush as heappush_, heappop as heappop_
from functools import partial
from itertools import product, chain


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        M, N = len(heightMap), len(heightMap[0])

        dirs = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        )

        # pre-mark the outer border as visited
        # and also have an extra row and column to serve as padding
        # to eliminate the need for boundary checks
        visited = [[True] * (N + 1)] + [
            [True] + [False] * (N - 2) + [True, True]
            for _ in range(M - 2)
        ] + [[True] * (N + 1)] * 2

        bfs_heap = []
        # heap operation aliases
        heappush = partial(heappush_, bfs_heap)
        heappop = partial(heappop_, bfs_heap)
        # add outer border to heap
        for i, j in chain(product(range(1, M - 1), (0, N - 1)), product((0, M - 1), range(N))):
            heappush((heightMap[i][j], i, j))

        ans = 0
        while bfs_heap:
            h, i, j = heappop()
            for di, dj in dirs:
                i_, j_ = i + di, j + dj
                if visited[i_][j_]:
                    continue
                visited[i_][j_] = True
                h_ = heightMap[i_][j_]
                ans += max(0, h - h_)
                heappush((max(h, h_), i_, j_))

        return ans
