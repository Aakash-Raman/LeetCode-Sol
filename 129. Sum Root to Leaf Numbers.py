# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None: return 0
        self.result = 0
        self.findsum(root, 0)
        return self.result
    
    def findsum(self, root, val):
        cur = val * 10 + root.val
        if(root.right == None and root.left == None):
            self.result += cur
            return
        if(root.left != None): self.findsum(root.left, cur) 
        if(root.right != None): self.findsum(root.right, cur)
