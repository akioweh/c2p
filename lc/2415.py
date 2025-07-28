"""
2415. Reverse Odd Levels of Binary Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        levels: list[list[TreeNode]] = [[root]]

        # bfs to transform b-tree into levels
        while True:
            cur_level = levels[-1]
            next_level: list[TreeNode] = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                levels.append(next_level)
            else:
                break

        # reverse
        for i, l in enumerate(levels):
            if i % 2:
                l.reverse()

        # reconstruct
        for cur_level, next_level in zip(levels, levels[1:]):
            for i, node in enumerate(cur_level):
                node.left = next_level[2 * i]
                node.right = next_level[2 * i + 1]

        return root
