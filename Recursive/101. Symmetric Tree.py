# first version
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
        
    def isMirror(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        
        if root1 == None or root2 == None:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left) 

 # second version   
class Solution:
def isSymmetric(self, root: TreeNode) -> bool:

    def isMirror(root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

    return isMirror(root,root)
