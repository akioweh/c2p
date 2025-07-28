"""
2924. Find Champion II
"""

class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        champions = set(range(n))
        for _, weak in edges:
            champions.discard(weak)
        if len(champions) == 1:
            return champions.pop()
        return -1

