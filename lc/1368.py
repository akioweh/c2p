"""
1368. Minimum Cost to Make at Least One Valid Path in a Grid
"""

from collections import deque


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = deque()
        costs = {}

        dp.append((0, 0, 0))
        while dp:
            nx, ny, cost = dp.popleft()
            while 0 <= nx < M and 0 <= ny < N and (nx, ny) not in costs:
                costs[nx, ny] = cost
                dp += [
                    (nx + dx, ny + dy, cost + 1)
                    for dx, dy in dirs
                ]
                dx, dy = dirs[grid[nx][ny] - 1]
                nx, ny = nx + dx, ny + dy

        return costs[M - 1, N - 1]
