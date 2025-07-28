"""
100. Same Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        else:
            res.append(None)
    return res

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        print(p)
        print(q)
        return serialize(p) == serialize(q)
