from typing import Iterable, TypeVar


class DisjointSet:
    """Disjoin Set data structure supporting union-find operations.

    This is an optimal implementation
    (in terms of asymptotic space and time complexity)
    """

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
        while (pox := parent_of[x]) != x:
            x, parent_of[x] = pox, parent_of[pox]
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
        # returns True for 0 or 1 arguments
        roots = map(self.find, args)
        r0 = next(roots, None)
        return all(r == r0 for r in roots)

    def size_of(self, x: int) -> int:
        return self.size[self.find(x)]

    def __len__(self) -> int:
        """Returns the number of disjoint sets"""
        return self.len


T: TypeVar = TypeVar('T')

class DisjointSetSparse:
    """Same as DisjointSet,
    but sets are indexed by arbitrary hashable objects
    instead of a contiguous range of integers.
    """

    __slots__ = ('parent', 'size', 'len')

    def __init__(self, ns: Iterable[T] = None):
        ns = ns or []
        self.parent = dict(zip(ns, ns))
        self.size = dict.fromkeys(ns, 1)
        self.len = len(self.parent)

    def add(self, n: T) -> bool:
        if n in self.parent:
            return False
        self.parent[n] = n
        self.size[n] = 1
        self.len += 1
        return True

    def find(self, x: T) -> T:
        parent_of = self.parent
        while (pox := parent_of[x]) != x:
            x, parent_of[x] = pox, parent_of[pox]
        return x

    def union(self, x: T, y: T) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.len -= 1
        return True

    def add_union(self, x: T, y: T) -> bool:
        """Shortcut for ``add(x); add(y); union(x, y)``"""
        self.add(x)
        self.add(y)
        return self.union(x, y)

    def same(self, *args: T) -> bool:
        roots = map(self.find, args)
        r0 = next(roots, None)
        return all(r == r0 for r in roots)

    def size_of(self, x: T) -> int:
        return self.size[self.find(x)]

    def __len__(self) -> int:
        return self.len

    def __contains__(self, item: T) -> bool:
        return item in self.parent

    def __iter__(self) -> Iterable[T]:
        return iter(self.parent)
