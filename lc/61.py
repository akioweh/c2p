"""
61. Rotate List
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None:
            return None

        N = 1
        cur = head
        while cur.next:
            cur = cur.next
            N += 1

        cur.next = head
        k %= N
        for _ in range(N - k):
            cur = cur.next

        head = cur.next
        cur.next = None
        return head
