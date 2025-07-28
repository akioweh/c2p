from collections.abc import Callable, Iterator, Sequence
from functools import reduce
from operator import ge, gt
from sys import maxsize
from typing import TypeVar

T = TypeVar('T')


class RURQ:
    """Range Update Range Query (RURQ) data structure.

    O(n) construction;
    Supports point updates (assignment),
    range map updates (addition), and
    range fold queries (any associative function)
    all in O(log n) time.

    This implementation fixes addition as the update operation,
    so only min/max really make sense as the fold function.
    """

    __slots__ = ('_default', '_func', '_sz', '_cache', 'data')

    def __init__(self, seq: Sequence[T], default: T = 0, func: Callable[[T, T], T] = max):
        """``func`` should be a binary associative function."""
        self._default = default
        self._func = func
        self._sz = ln = len(seq)
        self._cache = [0] * ln  # range-update tree
        self.data = [default] * ln + list(seq)  # range-query tree + leaves
        for i in reversed(range(ln)):
            self.data[i] = func(self.data[2 * i], self.data[2 * i + 1])

    def __len__(self) -> int:
        return self._sz

    def _conv_index(self, i: int | None, is_r: bool = False) -> int:
        """Converts conceptual index to leaf-node index.
        Supports negative indexing and checks bounds.
        """
        if i is None:
            i = self._sz if is_r else 0
        elif i < 0:
            i += self._sz
        if not 0 <= i < self._sz + is_r:
            raise IndexError('Index out of range')
        return i + self._sz

    def _push1(self, i: int):
        """Pushes (internal) node's lazy updates to its **direct** children."""
        if not (val := self._cache[i]):
            return
        self._cache[i] = 0
        self.data[l := i * 2] += val
        self.data[r := l + 1] += val
        if l < self._sz:
            self._cache[l] += val
            self._cache[r] += val

    def _push(self, i: int):
        """Propagates all updates on path from root to (leaf) node i"""
        for s in reversed(range(1, i.bit_length())):
            self._push1(i >> s)

    def _pull(self, i: int):
        """Recomputes internal nodes on path from (leaf) node i to root."""
        while i := i // 2:
            self.data[i] = self._func(self.data[2 * i], self.data[2 * i + 1]) + self._cache[i]

    def propagate(self):
        """Purges all cache; propagates all updates to leaves."""
        for i in range(self._sz):
            self._push1(i + self._sz)

    def collect(self, l: int | None, r: int | None, reverse: bool = False, push: bool = False) -> list[int]:
        """Collects the exact nodes representing the range ``data[l:r]``.
        Returns in left->right order to allow bisecting.
        """
        l, r = self._conv_index(l), self._conv_index(r, True)
        if push:
            self._push(l)
            self._push(r - 1)
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

    def update(self, l: int | None, r: int | None, val: T):
        """``map (+val)`` over ``data[l:r]``."""
        for i in self.collect(l, r):
            self.data[i] += val
            if i < self._sz:
                self._cache[i] += val
        l, r = self._conv_index(l), self._conv_index(r, True)
        self._pull(l)
        self._pull(r - 1)

    def query(self, l: int | None, r: int | None) -> T:
        """``fold func data[l:r]``"""
        return reduce(self._func, map(self.data.__getitem__, self.collect(l, r, push=True)), self._default)

    def __getitem__(self, i: int | slice) -> T:
        """Point or range fold queries."""
        if isinstance(i, slice):
            if i.step is not None:
                raise ValueError('Slice step not supported')
            return self.query(i.start, i.stop)
        i = self._conv_index(i)
        self._push(i)
        return self.data[i]

    def __setitem__(self, i: int, value: T):
        """Point update (assignment)."""
        i = self._conv_index(i)
        self._push(i)  # cache purge is needed as assignment is not associative/commutative
        self.data[i] = value
        self._pull(i)

    def __delitem__(self, i: int):
        self[i] = self._default

    def __iter__(self) -> Iterator[T]:
        self.propagate()
        return iter(self.data[self._sz :])

    def bound(self, value: int, l: int | None, r: int | None, comp: Callable[[T, T], bool], reverse: bool) -> int:
        data = self.data
        for i in self.collect(l, r, reverse, push=True):
            if comp(data[i], value):
                while i < self._sz:
                    self._push1(i)
                    i = nxt if comp(data[nxt := 2 * i + reverse], value) else nxt ^ 1
                return i - self._sz
        return l if reverse else r

    def lower_bound(self, value: int, l: int | None, r: int | None) -> int:
        """Locates the leftmost element ``>= value`` in ``data[l:r]``.
        Only makes sense for idempotent ``func``"""
        return self.bound(value, l, r, ge, False)

    def upper_bound(self, value: int, l: int | None, r: int | None) -> int:
        """Locates the leftmost element ``> value`` in ``data[l:r]``.
        Only makes sense for idempotent ``func``"""
        return self.bound(value, l, r, gt, False)


class RURQ_Max(RURQ):
    def __init__(self, seq: Sequence[int]):
        super().__init__(seq, -maxsize, max)


class RURQ_Min(RURQ):
    def __init__(self, seq: Sequence[int]):
        super().__init__(seq, maxsize, min)
