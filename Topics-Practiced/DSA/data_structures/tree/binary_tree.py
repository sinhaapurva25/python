class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# 2, 3, 4, 5

firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode