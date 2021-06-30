# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Postorder: left --> right --> mid
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
    
# Iterative
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [(root,False)], []
        
        while stack:
            node, visit = stack.pop()
            if node:
                if not visit:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                else:
                    res.append(node.val)
        return res
