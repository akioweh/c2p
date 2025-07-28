"""
1079. Letter Tile Possibilities
"""

from collections import Counter
from functools import reduce
from math import factorial
from operator import mul


class Solution:
    @staticmethod
    def n_perms(freqs: list[int]) -> int:
        return factorial(sum(freqs)) // reduce(mul, map(factorial, freqs), 1)

    def numTilePossibilities(self, tiles: str) -> int:
        multiset = Counter(tiles)
        N = len(multiset)
        max_freqs = list(multiset.values())
        cur_freqs = [0] * N
        ans = 0
        while True:
            ans += Solution.n_perms(cur_freqs)
            for i in range(N):
                if cur_freqs[i] < max_freqs[i]:
                    cur_freqs[i] += 1
                    break
                cur_freqs[i] = 0
            else:
                break

        return ans - 1  # subtract 1 for empty string
