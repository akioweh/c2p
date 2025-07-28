class BIT:
    """Binary Indexed Tree; aka. Fenwick Tree

    O(n) construction;
    Supports point updates, range fold queries,
    and bisection (on prefix folds)
    all in O(log n) time.

    Function must be associative and invertible.
    This implementation hardcodes addition.
    """

    __slots__ = ('_sz', 'data')

    def __init__(self, seq: list[int]):
        self._sz = len(seq)
        self.data = seq
        for i in range(self._sz):
            if (j := i | (i + 1)) < self._sz:
                seq[j] += seq[i]

    def update(self, i: int, value: int):
        """``data[i] += x``"""
        while i < len(self.data):
            self.data[i] += value
            i |= i + 1  # parent index

    def query(self, l: int, r: int) -> int:
        """``sum(data[l:r])``"""
        return self.query_r(r) - self.query_r(l)

    def query_r(self, r: int) -> int:
        """``sum(data[:r])``"""
        res = 0
        while r:
            res += self.data[r - 1]
            r &= r - 1  # left-"parent" index, (+)1-indexed
        return res

    def bisect_left(self, k: int) -> int:
        """Find leftmost i such that ``sum(data[:i]) >= k``"""
        i = -1
        msk = 1 << self._sz.bit_length()
        while msk := msk >> 1:
            if (j := i + msk) < self._sz and self.data[j] < k:
                k -= self.data[j]
                i = j
        return i + 1

    def bisect_right(self, k: int) -> int:
        """Find leftmost i such that ``sum(data[:i]) > k``"""
        i = -1
        msk = 1 << self._sz.bit_length()
        while msk := msk >> 1:
            if (j := i + msk) < self._sz and self.data[j] <= k:
                k -= self.data[j]
                i = j
        return i + 1
