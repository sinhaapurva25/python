# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = list()
        while l1 != None:
            list1.append(l1.val)
            l1 = l1.next

        list2 = list()
        while l2 != None:
            list2.append(l2.val)
            l2 = l2.next

        num1 = 0
        i = len(list1) - 1
        while i != -1:
            num1 = num1*10 + list1[i]
            i -= 1

        num2 = 0
        i = len(list2) - 1
        while i != -1:
            num2 = num2*10 + list2[i]
            i -= 1

        res=[int(i) for i in str(num1+num2)[::-1]]

        def list_to_LL(arr):
            if len(arr) < 1:
                return None

            if len(arr) == 1:
                return ListNode(arr[0])
            return ListNode(arr[0], next=list_to_LL(arr[1:]))

        return list_to_LL(res)
s = Solution()
s.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4])

# Next challenges:
# Add Binary
# Add Strings
# Add Two Numbers II
# Add to Array-Form of Integer
# Add Two Polynomials Represented as Linked Lists
# Double a Number Represented as a Linked List