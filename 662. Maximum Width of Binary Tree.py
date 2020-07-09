# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        result = 0
        queue = collections.deque()
        queue.append((root, 1))
        
        while queue:
            n = len(queue)
            result = max(result, queue[-1][1] - queue[0][1] + 1)
            
            while n > 0:
                node, pos = queue.popleft()
                
                if node.left:
                    queue.append((node.left, pos*2))
                
                if node.right:
                    queue.append((node.right, pos*2 + 1))
                
                n -= 1
        
        return result
        
