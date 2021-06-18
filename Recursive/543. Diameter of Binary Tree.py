# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.global_diameter = 0
        
        def depth(root):
            if root is None:
                return -1
            
            left = depth(root.left)
            right = depth(root.right)
            self.global_diameter = max(self.global_diameter, 2 + left + right)
            return 1 + max(left, right)
        
        depth(root)
        
        return self.global_diameter
