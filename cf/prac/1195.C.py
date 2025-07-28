from sys import stdin, stdout
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline
# noinspection PyShadowingBuiltins
print = stdout.write


def read_ints() -> Iterable[int]:
    return map(int, input().split())


N = int(input())
arr1 = list(read_ints())
arr2 = list(read_ints())

prev_col = [0, 0, 0]  # max height if we: [don't choose, choose from arr1, choose from arr2]

for i in range(N):
    prev_col[:] = (
        max(prev_col),
        max(prev_col[0], prev_col[2]) + arr1[i],
        max(prev_col[0], prev_col[1]) + arr2[i]
    )

print(f'{max(prev_col)}\n')
