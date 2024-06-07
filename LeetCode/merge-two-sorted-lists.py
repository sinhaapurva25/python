# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        m = len(list1)
        n = len(list2)
        i = j = k = 0
        merged_list = [0] * (m + n)

        while i < m and j < n:
            if list1[i] < list2[j]:
                merged_list[k] = list1[i]
                k += 1
                i += 1
            elif list1[i] > list2[j]:
                merged_list[k] = list2[j]
                k += 1
                j += 1
            else:
                merged_list[k] = list1[i]
                k += 1
                merged_list[k] = list2[j]
                k += 1
                i += 1
                j += 1
        if i < m:
            while i < m:
                merged_list[k] = list1[i]
                k += 1
                i += 1
        if j < n:
            while j < n:
                merged_list[k] = list2[j]
                k += 1
                j += 1
        return merged_list

s = Solution()
print(s.mergeTwoLists([-33, 0, 1, 3, 5], [-1, 2, 6]))
print(s.mergeTwoLists([0, 2, 4], [1, 3, 5]))
print(s.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))
print(s.mergeTwoLists(list1 = [], list2 = []))
print(s.mergeTwoLists(list1 = [], list2 = [0]))

