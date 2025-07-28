"""
515. Find Largest Value in Each Tree Row
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        res = []

        # traverse tree while keeping track of level (row)
        stack = [root]
        stack2 = [0]
        while stack:
            cur = stack.pop()
            cur_row = stack2.pop()
            if len(res) == cur_row:
                res.append(cur.val)
            else:
                res[cur_row] = max(res[cur_row], cur.val)

            if cur.left:
                stack.append(cur.left)
                stack2.append(cur_row + 1)
            if cur.right:
                stack.append(cur.right)
                stack2.append(cur_row + 1)

        return res
