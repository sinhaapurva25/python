from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while res != None and res.next!=None:
            if res.val == res.next.val:
                res.next = res.next.next
            else:
                res = res.next
        return head


s = Solution()
tc = [[1, 1, 2], [1, 1, 2, 3, 3], [1, 1, 1]]
# tc = [[1, 1, 1]]
for t in tc:
    # FROM LIST TO LISTNODE
    if len(t) > 0:
        tail = head = ListNode(t[0])
        for i in t[1:]:
            tail.next = ListNode(i)
            tail = tail.next
    else:
        head = None
    reversed_ll = s.deleteDuplicates(head)

    # FROM LISTNODE TO LIST
    tmp = reversed_ll
    arr = list()
    while tmp != None:
        arr.append(tmp.val)
        tmp = tmp.next
    print(arr)
