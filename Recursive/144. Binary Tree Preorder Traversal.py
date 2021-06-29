# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Preorder: mid --> left --> right
# Recursive
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

    
# Iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack, res = [root], []
        
        while stack:
            node = stack.pop()
            
            if node:
                res.append(node.val)
                # stack is LIFO, so root.right need to be first in and last out.
                stack.append(node.right)
                stack.append(node.left)
        return res
