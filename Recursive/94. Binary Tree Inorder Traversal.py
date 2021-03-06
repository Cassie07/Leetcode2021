# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inorder: left --> mid --> right
# Recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        self.res = []
        
        if not root:
                return self.res
            
        def helper(root):
            
            if root.left:
                helper(root.left)
            

            self.res.append(root.val)

            if root.right:
                helper(root.right)
            
                
        helper(root)
        
        return self.res

# iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack, res = [],[]
        
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            if not stack:
                return res
            
            node = stack.pop()
            res.append(node.val)
            root = node.right

            
