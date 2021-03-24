# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) != -1 
        
    def height(self,root):
        if root == None:
            return 0
        else:
            left = self.height(root.left)
            right = self.height(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return(max(self.height(root.left) + 1, self.height(root.right) + 1))
