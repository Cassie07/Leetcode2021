# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        self.res = []
        
        if not root:
            return []
        
        def helper(root):
            
            if root.left:
                helper(root.left)
                
            if root.right:
                helper(root.right)
            
            if root:
                self.res.append(root.val)
                
        helper(root)
        
        return self.res
