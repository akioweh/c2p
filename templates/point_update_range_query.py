from functools import reduce
from operator import ge, gt
from sys import maxsize
from typing import Callable, Iterator, Sequence, TypeVar

T = TypeVar('T')


class PURQ:
    """Point Update Range Query (PURQ) data structure.

    Supports point updates and range queries in O(log n) time.
    """

    __slots__ = ('_default', '_func', '_sz', 'data')

    def __init__(self, seq: Sequence[T], default: T = 0, func: Callable[[T, T], T] = max):
        """``func`` should (conceptually) be a (2+)-ary associative function."""
        self._default = default
        self._func = func
        self._sz = ln = len(seq)
        self.data = [default] * ln + list(seq)
        for i in reversed(range(ln)):
            self.data[i] = func(self.data[2 * i], self.data[2 * i + 1])

    def __len__(self) -> int:
        return self._sz

    def __iter__(self) -> Iterator[T]:
        return iter(self.data[self._sz:])

    def _conv_index(self, i: int | None, is_r: bool = False) -> int:
        """Converts conceptual index to leaf-node index.
        Supports negative indexing and checks bounds.
        """
        if i is None:
            return self._sz if is_r else 0
        if i < 0:
            i += self._sz
        if not 0 <= i < self._sz + is_r:
            raise IndexError('Index out of range')
        return i + self._sz

    def __getitem__(self, i: int | slice) -> T:
        """Point or range queries."""
        if isinstance(i, slice):
            if i.step is not None:
                raise ValueError('Slice step not supported')
            return self.query(i.start, i.stop)
        return self.data[self._conv_index(i)]

    def __setitem__(self, i: int, value: T):
        """Point updates."""
        i = self._conv_index(i)
        self.data[i] = value
        while i := i // 2:
            self.data[i] = self._func(self.data[2 * i], self.data[2 * i + 1])

    def __delitem__(self, i: int):
        self[i] = self._default

    def collect(self, l: int | None, r: int | None, reverse: bool = False) -> list[int]:
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

    def query(self, l: int | None = None, r: int | None = None) -> T:
        """``func(data[l:r])``"""
        return reduce(self._func, map(self.data.__getitem__, self.collect(l, r)), self._default)

    def bound(self, value: int, l: int | None, r: int| None, comp: Callable[[T, T], bool], reverse: bool) -> int:
        data = self.data
        for i in self.collect(l, r, reverse):
            if comp(data[i], value):
                while i < self._sz:
                    i = nxt if comp(data[nxt := 2 * i + reverse], value) else nxt ^ 1
                return i - self._sz
        return l if reverse else r

    def lower_bound(self, value: int, l: int | None = None, r: int | None = None) -> int:
        """Locates the leftmost element ``>= value`` in ``data[l:r]``"""
        return self.bound(value, l, r, ge, False)

    def upper_bound(self, value: int, l: int | None = None, r: int | None = None) -> int:
        """Locates the leftmost element ``> value`` in ``data[l:r]``"""
        return self.bound(value, l, r, gt, False)


class PURQ_Max(PURQ):
    def __init__(self, seq: Sequence[int]):
        super().__init__(seq, -maxsize, max)


class PURQ_Min(PURQ):
    def __init__(self, seq: Sequence[int]):
        super().__init__(seq, maxsize, min)
