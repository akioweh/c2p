"""
2658. Maximum Number of Fish in a Grid
"""


class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        # just fucking dfs

        M, N = len(grid), len(grid[0])

        def neighbors(__r, __c):
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ___r, ___c = __r + dr, __c + dc
                if 0 <= ___r < M and 0 <= ___c < N and grid[___r][___c]:
                    yield ___r, ___c

        seen = [[False] * N for _ in range(M)]
        max_fish = 0
        for r in range(M):
            for c in range(N):
                if seen[r][c] or not grid[r][c]:
                    continue
                cur_sum = 0
                stack = [(r, c)]
                while stack:
                    _r, _c = stack.pop()
                    if seen[_r][_c]:
                        continue
                    seen[_r][_c] = True
                    cur_sum += grid[_r][_c]
                    for _r_, _c_ in neighbors(_r, _c):
                        stack.append((_r_, _c_))
                max_fish = max(max_fish, cur_sum)

        return max_fish
