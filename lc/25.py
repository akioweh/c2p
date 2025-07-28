"""
25. Reverse Nodes in k-Group
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        def reverse_list(hd: ListNode, l: int) -> tuple[ListNode, ListNode, ListNode]:
            _nodes = []
            _cur = hd
            for _ in range(l):
                _nodes.append(_cur)
                _cur = _cur.next
                if _cur is None:
                    break
            if len(_nodes) < l:
                return hd, _nodes[-1], None
            _nodes[0].next = None
            for _i in range(len(_nodes) - 1, 0, -1):
                _nodes[_i].next = _nodes[_i - 1]
            return _nodes[-1], _nodes[0], _cur

        head, end, next_ = reverse_list(head, k)
        while next_ is not None:
            end.next, end, next_ = reverse_list(next_, k)

        return head
