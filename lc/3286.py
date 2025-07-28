"""
3286. Find a Safe Walk Through a Grid
"""
from heapq import heappop, heappush


def dijkstra_2dmtx(grid: list[list[float]], start: tuple[int, int]):
    m, n = len(grid), len(grid[0])
    dist = [
        [float('inf')] * n
        for _ in range(m)
    ]
    dist[start[0]][start[1]] = 0
    heap: list[tuple[float, tuple[int, int]]] = [(0, start)]
    while heap:
        d, (i, j) = heappop(heap)
        if d > dist[i][j]:
            continue
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            k, l = i + di, j + dj
            if not (0 <= k < m and 0 <= l < n):
                continue
            w = grid[k][l]
            if d + w < dist[k][l]:
                dist[k][l] = d + w
                heappush(heap, (dist[k][l], (k, l)))
    return dist


class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        return dijkstra_2dmtx(grid, (0, 0))[-1][-1] + grid[0][0] < health
