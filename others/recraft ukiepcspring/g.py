# a lazy max segtree. eat is update with -1.
# contents are sorted in increasing order.
class Eater:
    def __init__(self, seq: list[int]):
        self._sz = ln = len(seq)
        self.data = [0] * ln + list(seq)
        self.lazy = [0] * ln
        for i in reversed(range(1, ln)):
            self.data[i] = self.data[2 * i + 1]

    def _push1(self, i: int):
        if not (d := self.lazy[i]):
            return
        self.data[l := i * 2] += d
        self.data[r := l + 1] += d
        if l < self._sz:
            self.lazy[l] += d
            self.lazy[r] += d
        self.lazy[i] = 0

    def _push(self, i: int):
        for s in reversed(range(1, i.bit_length())):
            self._push1(i >> s)

    def _pull(self, i: int):
        while i := i // 2:
            self.data[i] = self.data[2 * i + 1] + self.lazy[i]

    def _collect(self, l: int, r: int) -> list[int]:
        nodes_l, nodes_r = [], []
        self._push(l)
        self._push(r - 1)
        while l < r:
            if l % 2:
                nodes_l.append(l)
                l += 1
            if r % 2:
                r -= 1
                nodes_r.append(r)
            l //= 2
            r //= 2
        nodes_r.reverse()
        return nodes_l + nodes_r

    def bisect_left(self, x: int) -> int:
        for i in self._collect(self._sz, 2 * self._sz):
            if self.data[i] >= x:
                while i < self._sz:
                    self._push1(i)
                    nxt = i * 2
                    if self.data[nxt] >= x:
                        i = nxt
                    else:
                        i = nxt + 1
                return i - self._sz
        return self._sz

    def eat(self, l: int):
        if l >= self._sz:
            return
        l += self._sz
        r = self._sz * 2
        for i in self._collect(l, r):
            self.data[i] -= 1
            if i < self._sz:
                self.lazy[i] -= 1
        self._pull(l)
        self._pull(r - 1)


def solve():
    N = read_int()
    candies = list(read_ints())
    M = read_int()
    shyness = read_ints()

    candies.sort()
    thingie = Eater(candies)

    ans = []
    for v in shyness:
        idx = thingie.bisect_left(v)
        thingie.eat(idx)
        ans.append(N - idx)

    write_str('\n'.join(map(str, ans)))
    write_str('\n')


### Python 3.8-3.13 compatible competitive programming template ###
# 4 Mar 2025 Version
from sys import stdin, stdout
from typing import Callable, Iterable, Iterator, Type

srdl = stdin.readline
swrt = stdout.write


def read_ints(int_t: Type[int] = int) -> Iterator[int]:
    """Reads a line as space-separated integers"""
    return map(int_t, srdl().split())


def read_int(int_t: Type[int] = int) -> int:
    """Reads a line as a single integer"""
    return int_t(srdl())


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


def prompt(msg: str, prefix: str = '? ', reader: Callable = read_str) -> str:
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return reader()


# Single-case format
if __name__ == '__main__':
    solve()
