from functools import reduce
from operator import ge, gt
from sys import maxsize
from typing import Callable, Iterator, Sequence, TypeVar

T = TypeVar('T')


class PURQ:
    """Point Update Range Query (PURQ) data structure.

    Supports point updates and range queries in O(log n) time.
    """

    def __init__(self, seq: Sequence[T], default: T = 0, func: Callable[[T, T], T] = max):
        """``func`` should (conceptually) be a (2+)-ary associative function."""
        self._default = default
        self._func = func
        self._sz = ln = len(seq)
        self.data = [default] * (2 * ln)
        self.data[ln:2 * ln] = seq
        for i in reversed(range(ln)):
            self.data[i] = func(self.data[2 * i], self.data[2 * i + 1])

    def __len__(self) -> int:
        return self._sz

    def __iter__(self) -> Iterator[T]:
        return iter(self.data[self._sz:])

    def _conv_index(self, i: int, excl_r: bool = False) -> int:
        """Converts conceptual index to leaf-node index.
        Supports negative indexing checks bounds.
        """
        if i < 0:
            i += self._sz
        if not 0 <= i < self._sz + excl_r:
            raise IndexError('Index out of range')
        return i + self._sz

    def __getitem__(self, i: int | slice) -> T:
        """Point or range queries."""
        if isinstance(i, slice):
            if i.step is not None:
                raise ValueError('Slice step not supported')
            l, r = i.start or 0, i.stop or self._sz
            return self.query(l, r)
        return self.data[self._conv_index(i)]

    def __setitem__(self, i: int, value: T):
        """Point updates."""
        i = self._conv_index(i)
        self.data[i] = value
        i //= 2
        while i:
            self.data[i] = self._func(self.data[2 * i], self.data[2 * i + 1])
            i //= 2

    def __delitem__(self, i: int):
        self[i] = self._default

    def _collect(self, l: int, r: int, reverse: bool = False) -> list[int]:
        l, r = self._conv_index(l), self._conv_index(r, True)
        nodes_l, nodes_r = [], []
        while l < r:
            if l % 2:
                nodes_l.append(l)
                l += 1
            if r % 2:
                r -= 1
                nodes_r.append(r)
            l //= 2
            r //= 2
        if reverse:
            nodes_l, nodes_r = nodes_r, nodes_l
        nodes_r.reverse()
        return nodes_l + nodes_r

    def query(self, l: int, r: int) -> T:
        """``func(data[l:r])``"""
        return reduce(self._func, map(self.data.__getitem__, self._collect(l, r)), self._default)


class PURQ_Max(PURQ):
    def __init__(self, seq: Sequence[int]):
        super().__init__(seq, -maxsize, max)

    def bound(self, value: int, l: int, r: int, comp: Callable[[int, int], bool], reverse: bool) -> int:
        data = self.data
        for i in self._collect(l, r, reverse):
            if comp(data[i], value):
                while i < self._sz:
                    i = 2 * i + reverse if comp(data[2 * i + reverse], value) else 2 * i + 1 - reverse
                return i - self._sz
        return l if reverse else r

    def lower_bound(self, value: int, l: int, r: int) -> int:
        """Find the leftmost value greater than or equal to val in the range [l, r).
        Returns r if not found.
        """
        return self.bound(value, l, r, ge, False)

    def upper_bound(self, value: int, l: int, r: int) -> int:
        """Find the leftmost value greater than val in the range [l, r).
        Returns r if not found.
        """
        return self.bound(value, l, r, gt, False)


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        N = len(baskets)
        capacities = PURQ_Max(baskets)

        ans = 0
        for amt in fruits:
            idx = capacities.lower_bound(amt, 0, N)
            if idx == N:
                ans += 1
            else:
                del capacities[idx]

        return ans
