"""
95. Unique Binary Search Trees II
"""

from functools import cache
from itertools import product


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    @cache
    def perms_bst(lo: int, hi: int) -> list[TreeNode | None]:
        if lo >= hi:
            return [None]
        if lo + 1 == hi:
            return [TreeNode(lo)]

        res = []
        for root in range(lo, hi):
            l_sts = Solution.perms_bst(lo, root)
            r_sts = Solution.perms_bst(root + 1, hi)
            for l_st, r_st in product(l_sts, r_sts):
                root_node = TreeNode(root)
                root_node.left = l_st
                root_node.right = r_st
                res.append(root_node)
        return res

    def generateTrees(self, n: int) -> list[TreeNode]:
        return Solution.perms_bst(1, n + 1)
