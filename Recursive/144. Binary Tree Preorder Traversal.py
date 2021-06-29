# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        self.res = []
        
        if not root:
            return []
        
        def helper(root):
            
            if root:
                self.res.append(root.val)
                
            if root.left:
                helper(root.left)
                
            if root.right:
                helper(root.right)
                
        helper(root)
        
        return self.res
