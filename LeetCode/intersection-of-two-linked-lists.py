from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1 = headA
        h2 = headB

        if h1 is None or h2 is None:
            return None

        while h1.val != h2.val or h1!=None or h2!= None:
            if h1.next == h2.next:
                return h1.next.val
            h1 = h1.next
            h2 = h2.next
        return None