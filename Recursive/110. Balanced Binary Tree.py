# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Version 1
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

# Version 2
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def height(node):
            if node is None:
                return 0
            else:
                left = height(node.left)
                right = height(node.right)
                # Extremely important! left == -1 or right == -1 means that an imbalanced subtree exists!!! if you not set it here, the nodes which higher than this sub-tree will get a wrong height
                if left == -1 or right == -1 or abs(left-right) > 1:
                    return -1
                else:
                    return 1+max(left, right)
                
        return height(root) != -1
