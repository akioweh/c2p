"""
83. Remove Duplicates from Sorted List
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        cur = head
        while True:
            while cur.next is not None and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
            if cur is None:
                return head
