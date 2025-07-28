"""
86. Partition List
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        p1_head = None
        p1_cur = None
        p2_head = None
        p2_cur = None
        cur = head
        while cur is not None:
            if cur.val < x:
                if p1_head is None:
                    p1_head = p1_cur = cur
                else:
                    p1_cur.next = p1_cur = cur
            else:
                if p2_head is None:
                    p2_head = p2_cur = cur
                else:
                    p2_cur.next = p2_cur = cur
            cur = cur.next
        if p1_head is None:
            return p2_head
        if p2_head is None:
            return p1_head
        p1_cur.next = p2_head
        p2_cur.next = None
        return p1_head
