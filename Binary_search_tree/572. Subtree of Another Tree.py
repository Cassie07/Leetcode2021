class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        def helper(root, subRoot):
            if not root and not subRoot:
                return True

            if not root or not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            
            if root.val == subRoot.val:
                return helper(root.left, subRoot.left) and helper(root.right, subRoot.right)
            
        if not root:
            return False
        
        if helper(root,subRoot): return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
