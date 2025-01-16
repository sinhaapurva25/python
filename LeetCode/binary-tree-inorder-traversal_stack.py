# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


root = TreeNode(1)
root.right = TreeNode(1, TreeNode(3, 2, 4), TreeNode(5, None, None))
root.right.left = TreeNode(3)

# Running the inorder traversal
s = Solution()
print(s.inorderTraversal(root))  # Output: [1, 3, 2]
