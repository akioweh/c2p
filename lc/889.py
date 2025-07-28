"""
889. Construct Binary Tree from Preorder and Postorder Traversal
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_node = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root_node

        rst_root_val = postorder[-2]
        st_partition = preorder.index(rst_root_val)
        root_node.right = self.constructFromPrePost(
            preorder[st_partition:],
            postorder[st_partition - 1:-1]
        )
        root_node.left = self.constructFromPrePost(
            preorder[1:st_partition],
            postorder[:st_partition - 1]
        )

        return root_node
