# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is not None:
            # res.append(root.left)
            self.helper(root.left, res)
            res.append(root.val)
            # res.append(root.right)
            self.helper(root.right, res)


root = TreeNode(1)
root.right = TreeNode(0, TreeNode(), TreeNode())
root.right.left = TreeNode(3)

# Running the inorder traversal
s = Solution()
print(s.inorderTraversal(root))  # Output: [1, 3, 2]
