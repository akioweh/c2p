"""
1028. Recover a Tree From Preorder Traversal
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        root_val, tmp, tr = traversal.partition('-')
        root = TreeNode(int(root_val))
        stack: list[TreeNode] = [root]
        tr += '-'  # auto-termination
        it = iter(tr)
        buf = [next(it)]
        next_depth = len(tmp)
        for ch in it:
            if (buf[0] == '-') == (ch == '-'):
                buf.append(ch)
            else:
                if buf[0] == '-':
                    next_depth = len(buf)
                else:
                    next_v = int(''.join(buf))
                    next_node = TreeNode(next_v)
                    if len(stack) == next_depth:
                        stack[-1].left = next_node
                    else:
                        while len(stack) > next_depth:
                            stack.pop()
                        stack[-1].right = next_node
                    stack.append(next_node)
                buf.clear()
                buf.append(ch)

        return root
