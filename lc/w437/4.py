from functools import cache


class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])

        dir_m = [
            (1, 1),
            (1, -1),
            (-1, -1),
            (-1, 1)
        ]

        def in_bounds(_i: int, _j: int) -> bool:
            return 0 <= _i < M and 0 <= _j < N

        max_possible = min((min(M, N) * 2 - 1), max(M, N))
        reached_max = False

        @cache
        def dfs(_i: int, _j: int, _dir: int = 0, has_turned: bool = False) -> int:
            nonlocal reached_max
            if reached_max:
                return 0
            cur_v = grid[_i][_j]
            next_v = 0 if cur_v == 2 else 2
            max_next = 0
            # same direction
            _di, _dj = dir_m[_dir]
            _ni, _nj = _i + _di, _j + _dj
            if in_bounds(_ni, _nj) and grid[_ni][_nj] == next_v:
                max_next = dfs(_ni, _nj, _dir, has_turned)
            # try turning
            if not has_turned:
                n_dir = (_dir + 1) % 4
                _di, _dj = dir_m[n_dir]
                _ni, _nj = _i + _di, _j + _dj
                if in_bounds(_ni, _nj) and grid[_ni][_nj] == next_v:
                    max_next = max(max_next, dfs(_ni, _nj, n_dir, True))
            if max_next + 1 == max_possible - 1:
                reached_max = True
            return max_next + 1

        max_len = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    if max_len == 0:
                        max_len = 1
                    for dir_ in range(4):
                        d_i, d_j = dir_m[dir_]
                        n_i, n_j = i + d_i, j + d_j
                        if in_bounds(n_i, n_j) and grid[n_i][n_j] == 2:
                            max_len = max(max_len, dfs(n_i, n_j, dir_) + 1)
                            if max_len == max_possible:
                                return max_len
        return max_len
