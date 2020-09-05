# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        ## RC ##
        ## APPROACH : RECURSION ##
        
        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##
        
        def helper(one, two):
            if(not one and not two):   return True
            if(not one or not two):    return False
            if(one.val != two.val):    return False
            return helper(one.left , two.right) and helper(one.right , two.left)
        
        if( not root ): return True
        return helper( root.left, root.right)
