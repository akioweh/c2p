from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N, M = read_ints()
    path = input().rstrip()
    grid = [
        list(read_ints())
        for _ in range(N)
    ]

    row_sum = [sum(row) for row in grid]
    col_sum = [sum(col) for col in zip(*grid)]

    # all_sum = x * m = x * n
    # => m = n, or x = 0
    # when m == n, x = all_sum / n
    # so if m != n, x = 0...
    # but what if m == n??
    # lets just say x = 0 anyway.

    i, j = 0, 0
    for d in path:
        if d == 'R':
            grid[i][j] = -col_sum[j]
            row_sum[i] -= col_sum[j]
            j += 1
        else:
            grid[i][j] = -row_sum[i]
            col_sum[j] -= row_sum[i]
            i += 1

    # bottom right corner
    if path[-1] == 'R':
        grid[i][j] = -col_sum[j]
    else:
        grid[i][j] = -row_sum[i]

    for row in grid:
        print(' '.join(map(str, row)))
