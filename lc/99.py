"""
99. Recover Binary Search Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        # inorder traversal
        stack = []
        cur = root
        prev = None
        first = None
        second = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev and prev.val > cur.val:
                if not first:
                    first = prev
                second = cur
            prev = cur
            cur = cur.right
        first.val, second.val = second.val, first.val
