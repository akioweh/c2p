"""
1765. Map of Highest Peak
"""

from collections import deque


class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        M, N = len(isWater), len(isWater[0])

        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        heights = [
            [-1] * N
            for _ in range(M)
        ]

        def land_neighbors_unseen(_i, _j):
            for _di, _dj in dirs:
                _ni, _nj = _i + _di, _j + _dj
                if 0 <= _ni < M and 0 <= _nj < N:
                    if heights[_ni][_nj] == -1:
                        yield _ni, _nj

        # find all water cells
        all_q = deque(filter(
            lambda ij: isWater[ij[0]][ij[1]] and (heights.__getitem__(ij[0]).__setitem__(ij[1], 0) or True),
            ((i, j) for i in range(M) for j in range(N))
        ))

        # parallel bfs from all water components
        while all_q:
            cur_i, cur_j = all_q.popleft()
            for nxt_i, nxt_j in land_neighbors_unseen(cur_i, cur_j):
                heights[nxt_i][nxt_j] = heights[cur_i][cur_j] + 1
                all_q.append((nxt_i, nxt_j))

        return heights