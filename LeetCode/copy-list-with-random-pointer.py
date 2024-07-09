from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = {None: None}
        cur = head
        while cur != None:
            copy = Node(cur.val)
            hash[cur] = copy
            cur = cur.next

        cur = head
        while cur != None:
            copy = hash[cur]
            copy.next = hash[cur.next]
            copy.random = hash[cur.random]
            cur = cur.next
        print(hash)
        return hash[head]


s = Solution()
tc = [[1, 2, 3, 4, 5], [1, 2], [1], []]
# tc = [[1]]
for t in tc:
    # FROM LIST TO LISTNODE
    if len(t) > 0:
        tail = head = Node(t[0])
        for i in t[1:]:
            tail.next = Node(i)
            tail = tail.next
    else:
        head = None
    reversed_ll = s.copyRandomList(head)

    # FROM LISTNODE TO LIST
    tmp = reversed_ll
    arr = list()
    while tmp != None:
        arr.append(tmp.val)
        tmp = tmp.next
    print(arr)