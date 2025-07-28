from itertools import pairwise

MOD = 998244353


def solve():
    N = read_int()
    parent = [-1, -1]
    parent.extend(read_ints())

    depth = [-1] * (N + 1)
    depth[1] = 0
    for i in range(2, N + 1):
        depth[i] = depth[parent[i]] + 1

    height = max(depth) + 1
    if height == 1:
        write_int(1)
        return

    layers = [[] for _ in range(height)]
    for i in range(1, N + 1):
        layers[depth[i]].append(i)

    dp = [0] * (N + 1)
    dp[1] = 1
    for v in layers[1]:
        dp[v] = 1

    for cur_layer, nxt_layer in pairwise(layers[1:]):
        layer_sum = sum(map(dp.__getitem__, cur_layer)) % MOD
        for v in nxt_layer:
            dp[v] = (layer_sum - dp[parent[v]]) % MOD

    write_int(sum(dp) % MOD)


### Python 3.8-3.13 compatible competitive programming template ###
# 21 Feb 2025 Version
from sys import stdin, stdout
from typing import Iterable, Iterator

srdl = stdin.readline
swrt = stdout.write


def read_ints() -> Iterator[int]:
    """Reads a line as space-separated integers"""
    return map(int, srdl().split())


def read_int() -> int:
    """Reads a line as a single integer"""
    return int(srdl())


def read_str() -> str:
    """Reads a line as-is"""
    return srdl().strip()


def write_ints(arr: Iterable[int]):
    """Writes a list of integers as a space-separated line"""
    swrt(' '.join(map(str, arr)))
    swrt('\n')


def write_int(val: int):
    """Writes a single integer as a line"""
    swrt(str(val))
    swrt('\n')


def write_str(val: str):
    """Writes a single string as a line"""
    swrt(val)
    swrt('\n')


def prompt(msg: str, prefix: str = '? ') -> str:
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return read_str()


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
