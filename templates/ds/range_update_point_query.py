from typing import Callable, Iterator, Sequence, TypeVar

T = TypeVar('T')


class RUPQ:
    """Range Update Point Query (RUPQ) data structure.

    Supports range updates and point queries in O(log n) time.
    """

    __slots__ = ('_default', '_func', '_sz', 'data', '_propagated')

    def __init__(self, seq: Sequence[T], default: T = 0, func: Callable[[T, T], T] = max):
        """``func`` should (conceptually) be a (2+)-ary associative AND commutative function."""
        self._default = default
        self._func = func
        self._sz = ln = len(seq)
        self.data = [default] * ln + list(seq)
        self._propagated = True

    def __len__(self) -> int:
        return self._sz

    def __iter__(self) -> Iterator[T]:
        if not self._propagated:
            self.propagate()
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

    def __getitem__(self, i: int) -> T:
        """Point queries."""
        i = self._conv_index(i)
        if self._propagated:
            return self.data[i]
        res = self._default
        while i:
            res = self._func(res, self.data[i])
            i //= 2
        return res

    def __setitem__(self, i: int | slice, value: T):
        """Point or range updates.
        Note that this is not assignment, but modification through ``func``.
        """
        if isinstance(i, int):
            i = self._conv_index(i)
            self.data[i] = self._func(self.data[i], value)
        else:
            if i.step is not None:
                raise ValueError('Slice step not supported')
            self.update(i.start, i.stop, value)

    def propagate(self):
        data = self.data
        func = self._func
        for i in range(1, self._sz):
            data[i * 2] = func(data[i * 2], data[i])
            data[i * 2 + 1] = func(data[i * 2 + 1], data[i])
            data[i] = self._default
        self._propagated = True

    def update(self, l: int, r: int, value: T):
        """Set ``data[l:r]`` to `value``."""
        l, r = self._conv_index(l), self._conv_index(r, True)
        while l < r:
            if l % 2:
                self.data[l] = self._func(value, self.data[l])
                l += 1
            if r % 2:
                r -= 1
                self.data[r] = self._func(self.data[r], value)
            l //= 2
            r //= 2
        self._propagated = False
