# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = list()
        while list1 != None:
            arr1.append(list1.val)
            list1 = list1.next

        arr2 = list()
        while list2 != None:
            arr2.append(list2.val)
            list2 = list2.next

        len_a = len(arr1)
        len_b = len(arr2)
        arr = [0]*(len_a+len_b)

        i = j = k = 0

        while i < len_a and j < len_b:
            if arr1[i] <= arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1
            k += 1

        while i < len_a:
            arr[k] = arr1[i]
            i += 1
            k += 1

        while j < len_b:
            arr[k] = arr2[j]
            j += 1
            k += 1

        current = ListNode(arr[0])
        for v in arr[1:]:
            current.next = ListNode(v)
            current = current.next

        return current


s = Solution()
print(s.mergeTwoLists(ListNode(-33, 0, 1, 3, 5), ListNode[-1, 2, 6]))
print(s.mergeTwoLists([0, 2, 4], [1, 3, 5]))
print(s.mergeTwoLists([1,2,4], [1,3,4]))
print(s.mergeTwoLists([], []))
print(s.mergeTwoLists([], [0]))

# Next challenges:
# Merge k Sorted Lists
# Sort List
# Shortest Word Distance II
# Add Two Polynomials Represented as Linked Lists
# Longest Common Subsequence Between Sorted Arrays
# Merge Two 2D Arrays by Summing Values