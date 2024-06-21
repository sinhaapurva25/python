from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse it
        # Remove nth node
        # Reverse it
        head_of_reversed_ll = None
        while head != None:
            tmp = head.next
            head.next = head_of_reversed_ll
            head_of_reversed_ll = head
            head = tmp

        if n == 1:
            head_of_reversed_ll = head_of_reversed_ll.next

        head = None
        i = 0
        while head_of_reversed_ll != None:
            if i == n - 2 and n != 1:
                tmp = head_of_reversed_ll.next.next
            else:
                tmp = head_of_reversed_ll.next
            head_of_reversed_ll.next = head
            head = head_of_reversed_ll
            head_of_reversed_ll = tmp
            i += 1
        return head


s = Solution()
tc = [
        [[28, 39, 74, 25, 78, 33, 60], 1, [28, 39, 74, 25, 78, 33]],
        [[28, 39, 74, 25, 78, 33, 60], 2, [28, 39, 74, 25, 78, 60]],
        [[1], 1, []]
     ]
for test_case in tc:
    t = test_case[0]
    n = test_case[1]
    expected = test_case[2]
    print("Input: {}, n:{}".format(t, n))
    if len(t) < 1:
        head = None
    else:
        tail = head = ListNode(t[0])
        for i in t[1:]:
            tail.next = ListNode(i)
            tail = tail.next
    node_removed = s.removeNthFromEnd(head, n)

    output = list()
    while node_removed != None:
        output.append(node_removed.val)
        node_removed = node_removed.next
    print("Output: {}".format(output))
    print("Expected: {}".format(expected))
    print("*** Test Case", end="")
    if output == expected:
        print(" Passed ***")
    else:
        print(" Failed ***")