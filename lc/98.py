"""
98. Validate Binary Search Tree
"""


def t_max(root):
    while root.right:
        root = root.right
    return root


def t_min(root):
    while root.left:
        root = root.left
    return root


class Solution:
    def isValidBST(self, root) -> bool:
        if root.left is not None:
            if not self.isValidBST(root.left) or t_max(root.left).val >= root.val:
                return False
        if root.right is not None:
            if not self.isValidBST(root.right) or t_min(root.right).val <= root.val:
                return False
        return True
