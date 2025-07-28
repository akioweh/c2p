"""
92. Reverse Linked List II
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tmp = ListNode(next=head)
        l_head = tmp
        for _ in range(left - 1):
            l_head = l_head.next

        cur = l_head.next
        to_reverse = []
        for _ in range(right - left + 1):
            to_reverse.append(cur)
            cur = cur.next

        r_head = cur

        for i in range(len(to_reverse) - 1, 0, -1):
            to_reverse[i].next = to_reverse[i - 1]

        to_reverse[0].next = r_head
        l_head.next = to_reverse[-1]

        return tmp.next
