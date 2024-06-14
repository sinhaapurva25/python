# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_sorted_lists(self, a, b):

        len_a = len(a)
        len_b = len(b)
        arr = [0] * (len_a + len_b)

        i = j = k = 0

        while i < len_a and j < len_b:
            if a[i] <= b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1

        while i < len_a:
            arr[k] = a[i]
            i += 1
            k += 1

        while j < len_b:
            arr[k] = b[j]
            j += 1
            k += 1

        return arr

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]

        # CONVERT THE LIST OF LISTNODES TO A 2D LIST
        arrays = list()
        for head in lists:
            arr = list()
            while head != None:
                arr.append(head.val)
                head = head.next
            arrays.append(arr)

        # MERGE K SORTED LISTS
        arr_1_2 = list()
        if len(arrays) > 1:
            arr_1 = arrays[0]
            for i in range(1, len(arrays)):
                arr_2 = arrays[i]
                arr_1_2 = self.merge_two_sorted_lists(arr_1, arr_2)
                arr_1 = arr_1_2

        # CONVERT THE MERGED LIST TO LISTNODE
        if len(arr_1_2) > 0:
            tail = head = ListNode(arr_1_2[0])
            for x in arr_1_2[1:]:
                tail.next = ListNode(x)
                tail = tail.next
        else:
            head = None
        return head


s = Solution()
tc1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = list()
for tc in tc1:
    # FROM LIST TO LISTNODE
    tail = head = ListNode(tc[0])
    for x in tc[1:]:
        tail.next = ListNode(x)  # Create and add another node
        tail = tail.next  # Move the tail pointer
    lists.append(head)
    # print(head)
    # FROM LISTNODE TO LIST
    # arr = list()
    # while head != None:
    #     arr.append(head.val)
    #     head = head.next
    # print(arr)

# CONVERT A LIST OF LISTNODES TO A 2D LIST
# arrays = list()
# for head in lists:
#     arr = list()
#     while head != None:
#         arr.append(head.val)
#         head = head.next
#     print(arr)
#     arrays.append(arr)
# print(arrays)

print(s.mergeKLists(lists))

# Next challenges:
# Ugly Number II
# Smallest Subarrays With Maximum Bitwise OR
