# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            if root is None:
                return []
            left = inorder(root.left)
            val = [root.val]
            right = inorder(root.right)
            return left + val + right
        return inorder(root)[k-1]
