# Python3 Program to print binary tree in 2D
COUNT = [10]

# Binary Tree Node
""" utility that allocates a newNode
with the given key """
class newNode:

	# Construct to create a newNode
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root, space) :

	# Base case
	if (root == None) :
		return

	# Increase distance between levels
	space += COUNT[0]

	# Process right child first
	print2DUtil(root.right, space)

	# Print current node after space
	# count
	print()
	for i in range(COUNT[0], space):
		print(end = " ")
	print(root.data)

	# Process left child
	print2DUtil(root.left, space)

# Wrapper over print2DUtil()
def print2D(root) :
	
	# space=[0]
	# Pass initial space count as 0
	print2DUtil(root, 0)

# Driver Code
if __name__ == '__main__':

	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)

	root.left.left = newNode(4)
	root.left.right = newNode(5)
	root.right.left = newNode(6)
	root.right.right = newNode(7)

	# root.left.left.left = newNode(8)
	# root.left.left.right = newNode(9)
	# root.left.right.left = newNode(10)
	# root.left.right.right = newNode(11)
	# root.right.left.left = newNode(12)
	# root.right.left.right = newNode(13)
	# root.right.right.left = newNode(14)
	# root.right.right.right = newNode(15)
	
	print2D(root)