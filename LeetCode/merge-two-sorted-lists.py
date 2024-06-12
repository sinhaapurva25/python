# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)  # curr is the curr pointer for our DUMMY

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next

            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        # now we 'll see if there are still some elements left then we ll add them as well
        if list1: curr.next = list1

        if list2: curr.next = list2

        return dummy.next

s = Solution()
print(s.mergeTwoLists([-33, 0, 1, 3, 5], [-1, 2, 6]))
print(s.mergeTwoLists([0, 2, 4], [1, 3, 5]))
print(s.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))
print(s.mergeTwoLists(list1 = [], list2 = []))
print(s.mergeTwoLists(list1 = [], list2 = [0]))

