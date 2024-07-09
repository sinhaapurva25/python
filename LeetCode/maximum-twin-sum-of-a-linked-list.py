from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = list()
        while head != None:
            arr.append(head.val)
            head = head.next
        res = float("-inf")
        for i in range(len(arr)):
            res = max(res, arr[i] + arr[len(arr) - i - 1])
        return res


s = Solution()
tc = [[1, 2, 3, 4, 5, 4, 3, 2, 1], [1, 2, 3, 4, 4, 3, 2, 1],[1, 2, 2, 1], [1, 2], [1], [], [1,1,2,1]]
for t in tc:
    # FROM LIST TO LISTNODE
    if len(t) > 0:
        tail = head = ListNode(t[0])
        for i in t[1:]:
            tail.next = ListNode(i)
            tail = tail.next
    else:
        head = None
    max_twin_sum = s.pairSum(head)

    print("Max twin sum of {} is {}".format(t, max_twin_sum))