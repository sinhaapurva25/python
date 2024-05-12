# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        head_arr = list()
        while head!= None:
            head_arr.append(head)
            head = head.next
        return head_arr[len(head_arr)//2]
s = Solution()
print(s.middleNode(head = [1,2,3,4,5]))
print(s.middleNode(head = [1,2,3,4,5,6]))

# Next challenges:
# Delete the Middle Node of a Linked List
# Maximum Twin Sum of a Linked List
