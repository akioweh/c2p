from bisect import bisect_left, insort
from sys import stdin, stdout

# noinspection PyShadowingBuiltins
input = stdin.readline
# noinspection PyShadowingBuiltins
print = stdout.write


def read_ints():
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(read_ints())

    for i in range(N - 1):
        lo, hi = min(arr[i], arr[i + 1]), max(arr[i], arr[i + 1])
        if lo * 2 > hi:
            print('YES\n')
            break
    else:
        print('NO\n')
