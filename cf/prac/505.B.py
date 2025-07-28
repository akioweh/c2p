class DisjointSet:
    __slots__ = ('parent', 'size', 'len')

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.len = n

    def find(self, x: int) -> int:
        # Here we use a better Path Splitting algorithm
        # by Tarjan / Van Leeuwen
        # instead of the standard recursive implementation.
        # This uses O(1) space and has a better practical runtime
        # ... and, of course, is not recursive!
        parent_of = self.parent
        while parent_of[x] != x:
            x, parent_of[x] = parent_of[x], parent_of[parent_of[x]]
        return x

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False

        if self.size[x] < self.size[y]:
            x, y = y, x

        self.parent[y] = x
        self.size[x] += self.size[y]
        self.len -= 1
        return True

    def same(self, *args: int) -> bool:
        roots = map(self.find, args)
        r0 = next(roots, None)
        return all(r == r0 for r in roots)

    def __len__(self) -> int:
        return self.len


def solve():
    N, M = read_ints()
    colors = [DisjointSet(N + 1) for _ in range(M + 1)]
    for _ in range(M):
        u, v, color = read_ints()
        colors[color].union(u, v)

    Q = read_int()
    for _ in range(Q):
        u, v = read_ints()
        write_int(sum(
            colors[i].same(u, v)
            for i in range(M + 1)
        ))


### Python 3.8-3.13 compatible competitive programming template ###
# 21 Jan 2025 Version
from sys import stdin, stdout
from typing import Iterable, List

srdl = stdin.readline
swrt = stdout.write


def read_ints() -> Iterable[int]:
    """Reads a line as space-separated integers"""
    return map(int, srdl().split())


def read_int() -> int:
    """Reads a line as a single integer"""
    return int(srdl())


def read_str() -> str:
    """Reads a line as-is"""
    return srdl().strip()


def read_strs() -> List[str]:
    """Reads a line as space-separated strings"""
    return srdl().split()


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


# Single-case format
if __name__ == '__main__':
    solve()
