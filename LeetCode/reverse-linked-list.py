# https://www.geeksforgeeks.org/reverse-a-linked-list/

# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev


s = Solution()
tc = [[1, 2, 3, 4, 5], [1, 2], [1], []]
for t in tc:
    # FROM LIST TO LISTNODE
    if len(t) > 0:
        tail = head = ListNode(t[0])
        for i in t[1:]:
            tail.next = ListNode(i)
            tail = tail.next
    else:
        head = None
    reversed_ll = s.reverseList(head)

    # FROM LISTNODE TO LIST
    tmp = reversed_ll
    arr = list()
    while tmp != None:
        arr.append(tmp.val)
        tmp = tmp.next
    print(arr)