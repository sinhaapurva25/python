from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseLinkedList(self, ll: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while ll != None:
            next = ll.next
            ll.next = prev
            prev = ll
            ll = next
        return prev
    def linkedListToNumber(self, ll: Optional[ListNode]) -> int:
        i = 0
        n = 0
        while ll != None:
            n += int(ll.val) * 10 ** i
            i += 1
            ll = ll.next
        return n

    def listToLinkedList(self, l: List) -> Optional[ListNode]:
        if len(l) > 0:
            tail = head = ListNode(l[0])
            for i in l[1:]:
                tail.next = ListNode(i)
                tail = tail.next
        else:
            head = None
        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num1 = self.linkedListToNumber(l1)
        l2_num2 = self.linkedListToNumber(l2)
        res = self.reverseLinkedList(self.listToLinkedList(list(str(l1_num1+l2_num2))))
        return res


s = Solution()
print(s.addTwoNumbers(s.listToLinkedList([2, 4, 3]), s.listToLinkedList([5, 6, 4])))

# Next challenges:
# Add Binary
# Add Strings
# Add Two Numbers II
# Add to Array-Form of Integer
# Add Two Polynomials Represented as Linked Lists
# Double a Number Represented as a Linked List

# More challenges
# 415. Add Strings
# 445. Add Two Numbers II
# 989. Add to Array-Form of Integer