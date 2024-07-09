from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast_pointer = slow_pointer = head
        while fast_pointer != None and fast_pointer.next != None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False

# It's not possible o check this code on local
# You are not defining which node points to which node next
