from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ll = head
        arr = list()
        while ll!=None:
            arr.append(ll.val)
            ll = ll.next
        # print("input arr", arr)

        if len(arr) > 2:
            i = 0
            arr_reordered = [arr[len(arr)//2]]*len(arr)
            while i < (len(arr)//2):
                arr_reordered[i*2] = arr[i]
                arr_reordered[i*2 + 1] = arr[len(arr) - i - 1]
                i += 1
            # print("arr_reordered", arr_reordered)
            arr[:] = arr_reordered[:]
            arr_reordered.clear()


            i = 0
            while i < len(arr):
                head.val = arr[i]
                head = head.next
                i += 1
        # else:
            # print("arr not needed reordering", arr)


s = Solution()
tc = [[1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2], [1], []]
for t in tc:
    # FROM LIST TO LISTNODE
    if len(t) > 0:
        tail = head = ListNode(t[0])
        for i in t[1:]:
            tail.next = ListNode(i)
            tail = tail.next
    else:
        head = None
    s.reorderList(head)

    # FROM LISTNODE TO LIST
    tmp = head
    arr = list()
    while tmp != None:
        arr.append(tmp.val)
        tmp = tmp.next
    print(arr)
