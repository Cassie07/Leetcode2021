# Recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        self.res = []
        if not root:
            return []
        
        def helper(root):
            
            if root.left:
                helper(root.left)
            
            self.res.append(root.val)
            
            if root.right:
                helper(root.right)
        
        helper (root)
        
        return self.res
