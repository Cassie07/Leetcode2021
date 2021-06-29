# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS (recursive)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        self.res = 0
        
        def helper(root, k):
            if root.left:
                k = helper(root.left, k)
                
                
            k -= 1
            if k == 0:
                self.res = root.val
                return k


            if root.right:
                k = helper(root.right, k)
            
            return k
                
        helper(root,k)
        
        return self.res
