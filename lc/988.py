"""
988. Smallest String Starting From Leaf
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        smallest = [26]  # larger than any valid value
        # iterative dfs, while keeping track of path
        stack = [(root, [root.val])]
        while stack:
            node, path = stack.pop()
            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if node.left:
                stack.append((node.left, path + [node.left.val]))
            if not node.left and not node.right:
                smallest[:] = min(
                    smallest,
                    path[::-1]
                )
        return ''.join(chr(ord('a') + i) for i in smallest)
