"""
1261. Find Elements in a Contaminated Binary Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    @staticmethod
    def dfs(node: TreeNode, cur_val: int = 0):
        yield cur_val
        if node.left:
            yield from FindElements.dfs(node.left, 2 * cur_val + 1)
        if node.right:
            yield from FindElements.dfs(node.right, 2 * cur_val + 2)

    def __init__(self, root: TreeNode):
        self.vals = set(FindElements.dfs(root))

    def find(self, target: int) -> bool:
        return target in self.vals
