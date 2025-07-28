"""
96. Unique Binary Search Trees
"""

from functools import cache


@cache
def num_trees(lo: int, hi: int) -> int:
    if lo + 1 >= hi:
        return 1

    res = 0
    for root in range(lo, hi):
        n_ltrees = num_trees(lo, root)
        n_rtrees = num_trees(root + 1, hi)
        res += n_ltrees * n_rtrees

    return res


class Solution:
    def numTrees(self, n: int) -> int:
        return num_trees(1, n + 1)
