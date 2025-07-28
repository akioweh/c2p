"""
ST?.. but it is not a segment tree!
"""

from itertools import starmap
from typing import Callable, Sequence, TypeVar

T = TypeVar('T')


class SparseTable:
    """Range Query data structure.

    O(n log n) construction;
    O(log n) query, or O(1) for idempotent functions.
    """

    def __init__(self, seq: Sequence[T], func: Callable[[T, T], T] = min, is_idempotent: bool = True):
        """``func`` should (conceptually) be a (2+)-ary associative function."""
        self._ln = len(seq)
        self._K = self._ln.bit_length() - 1  # max k such that 2**k <= n
        self._func = func
        self._data = [cur_row := list(seq)]  # data[k][l] = func(seq[l:l + 2**k])
        step = 1
        while cur_row := list(starmap(func, zip(cur_row, cur_row[step:]))):
            self._data.append(cur_row)
            step *= 2
        self.query: Callable[[int, int], T] = self.query_idmpt if is_idempotent else self.query_

    def __getitem__(self, i: int) -> T:
        return self._data[0][i]

    def query_(self, l: int, r: int) -> T:
        """(O log n) ``func(seq[l:r])`` for general ``func``"""
        if not 0 <= l < r <= self._ln:
            raise IndexError('Index out of range')
        res = 0
        for k in reversed(range(self._K + 1)):
            if (step := 1 << k) <= r - l:
                res = self._func(res, self._data[k][l])
                l += step
        return res

    def query_idmpt(self, l: int, r: int) -> T:
        """O(1) ``func(seq[l:r])`` for idempotent ``func``"""
        if not 0 <= l < r <= self._ln:
            raise IndexError('Index out of range')
        k = (r - l).bit_length() - 1
        return self._func(self._data[k][l], self._data[k][r - (1 << k)])


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    rmq = SparseTable(arr)
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        print(rmq.query(l, r + 1))


if __name__ == '__main__':
    solve()
