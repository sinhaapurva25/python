from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None

        arr = list()
        while head!= None:
            arr.append(head.val)
            head = head.next
        frq = dict()
        for i in arr:
            frq[i] = 1 + frq.get(i, 0)
        arr = [k for k,v in frq.items() if v == 1]

        if len(arr) > 0:
            tail = res = ListNode(arr[0])
            for i in arr[1:]:
                tail.next = ListNode(i)
                tail = tail.next
        else:
            res = None
        return res

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


