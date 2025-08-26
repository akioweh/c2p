"""
ST?.. but it is not a segment tree!
"""

from itertools import starmap
from typing import Callable, Sequence, TypeVar

T = TypeVar('T')


class SparseTable:
    """Range Query data structure.

    O(n log n) construction;
    O(log n) range fold queries, or O(1) for idempotent function.
    """

    def __init__(self, seq: Sequence[T], func: Callable[[T, T], T] = min, is_idempotent: bool = True):
        """``func`` should be a binary associative function."""
        self._ln = len(seq)
        self._K = self._ln.bit_length() - 1  # max k such that 2**k <= n
        self._func = func
        self._data = [cur_row := list(seq)]  # data[k][l] = func(seq[l:l + 2**k])
        step = 1
        while cur_row := list(starmap(func, zip(cur_row, cur_row[step:]))):
            self._data.append(cur_row)
            step *= 2
        self.query: Callable[[int, int], T] = self.query_idmpt if is_idempotent else self.query

    def __getitem__(self, x: int | slice) -> T:
        """Point or range fold queries."""
        if isinstance(x, slice):
            if x.step is not None:
                raise ValueError('Slice step not supported')
            return self.query(*self._conv_slice(x.start, x.stop))
        return self._data[0][x]

    def _conv_slice(self, l: int | None, r: int | None) -> tuple[int, int]:
        if l is None:
            l = 0
        elif l < 0:
            l += self._ln
        if r is None:
            r = self._ln
        elif r < 0:
            r += self._ln
        if not 0 <= l < r <= self._ln:
            raise IndexError('Invalid slice')
        return l, r

    def query(self, l: int, r: int) -> T:
        """O(log n) ``fold func seq[l:r]``"""
        res = 0
        for k in reversed(range(self._K + 1)):
            if (step := 1 << k) <= r - l:
                res = self._func(res, self._data[k][l])
                l += step
        return res

    def query_idmpt(self, l: int, r: int) -> T:
        """O(1) ``fold func seq[l:r]`` for idempotent ``func``"""
        k = (r - l).bit_length() - 1
        return self._func(self._data[k][l], self._data[k][r - (1 << k)])
