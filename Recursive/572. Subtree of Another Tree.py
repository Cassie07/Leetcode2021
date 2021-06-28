# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# key points
# 1. Similar to 100. same tree
# 2. 判别条件： root.val == subRoot.val and root.left.val == subRoot.left.val and root.right.val == subRoot.right.val

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        if not root:
            return False
        
        def isSame(root, subRoot):
            if not root and not subRoot: return True

            if not root or not subRoot: return False

            if root.val != subRoot.val: return False
            
            return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
        
        if isSame(root, subRoot): return True
        
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot) 
