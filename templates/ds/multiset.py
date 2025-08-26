from typing import Iterable


class LCAlphMultiSet:
    """Multiset for lowercase english letters"""

    __slots__ = ('counts',)

    def __init__(self, cs: Iterable[str] = None):
        self.counts = [0] * 26
        if cs is not None:
            for c in cs:
                self.add(c)

    @classmethod
    def from_array(cls, arr: list[int]):
        self = cls()
        self.counts = arr
        return self

    def add(self, c: str):
        x = ord(c) - 97
        self.counts[x] += 1

    def remove(self, c: str):
        x = ord(c) - 97
        self.counts[x] -= 1

    def delete(self, c: str):
        x = ord(c) - 97
        self.counts[x] = 0

    def __getitem__(self, c: str) -> int:
        x = ord(c) - 97
        return self.counts[x]

    def __setitem__(self, c: str, v: int):
        x = ord(c) - 97
        self.counts[x] = v

    def __len__(self) -> int:
        return sum(self.counts)

    def __bool__(self) -> bool:
        return any(self.counts)

    def __iter__(self):
        for i, c in enumerate(self.counts):
            if c:
                yield chr(i + 97)

    def __contains__(self, c: str) -> bool:
        return self.counts[ord(c) - 97] > 0

    def __eq__(self, other) -> bool:
        return self.counts == other.counts

    def __ne__(self, other) -> bool:
        return self.counts != other.counts

    def __and__(self, other):
        return LCAlphMultiSet.from_array([min(a, b) for a, b in zip(self.counts, other.counts)])

    def __or__(self, other):
        return LCAlphMultiSet.from_array([max(a, b) for a, b in zip(self.counts, other.counts)])

    def __sub__(self, other):
        return LCAlphMultiSet.from_array([max(a - b, 0) for a, b in zip(self.counts, other.counts)])

    def __add__(self, other):
        return LCAlphMultiSet.from_array([a + b for a, b in zip(self.counts, other.counts)])

    def __gt__(self, other) -> bool:
        return any(a > b for a, b in zip(self.counts, other.counts))

    def __lt__(self, other) -> bool:
        return any(a < b for a, b in zip(self.counts, other.counts))

    def __ge__(self, other) -> bool:
        return all(a >= b for a, b in zip(self.counts, other.counts))

    def __le__(self, other) -> bool:
        return all(a <= b for a, b in zip(self.counts, other.counts))

    def __hash__(self):
        return hash(tuple(self.counts))
