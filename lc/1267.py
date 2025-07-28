"""
1267. Count Servers that Communicate
"""

from operator import itemgetter


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        row_col_idx = [-1] * M
        col_row_idx = [-1] * N

        ans = 0
        for i, r in enumerate(grid):
            for j, _ in filter(itemgetter(1), enumerate(r)):
                rc = row_col_idx[i]
                cc = col_row_idx[j]

                if rc == cc == -1:  # new isolated
                    row_col_idx[i] = j
                    col_row_idx[j] = i
                    continue

                ans += 1  # row or col populated
                if rc >= 0:  # row has isolated member; add 1 to ans and unmark corresponding col
                    col_row_idx[rc] = -2
                    ans += 1
                if cc >= 0:
                    row_col_idx[cc] = -2
                    ans += 1

                # mark row and col as populated
                row_col_idx[i] = col_row_idx[j] = -2

        return ans
