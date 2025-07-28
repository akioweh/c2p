"""
2349. Design a Number Container System
"""

from collections import defaultdict

from sortedcontainers import SortedSet


class NumberContainers:

    def __init__(self):
        self.indices_of: dict[int, SortedSet[int]] = defaultdict(SortedSet)
        self.value_at: dict[int, int] = {}

    def change(self, index: int, number: int) -> None:
        # delete if already exists
        if index in self.value_at:
            prev = self.value_at[index]
            self.indices_of[prev].remove(index)
            if not self.indices_of[prev]:
                del self.indices_of[prev]

        # add new value
        self.value_at[index] = number
        self.indices_of[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.indices_of:
            return -1
        return self.indices_of[number][0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
