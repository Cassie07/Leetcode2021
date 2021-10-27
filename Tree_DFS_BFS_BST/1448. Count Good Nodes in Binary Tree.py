class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0
        
        def BST(root, max_value):
            
            if not root:
                return
            
            if root.val >= max_value:
                max_value = root.val
                self.res += 1
                
            BST(root.left, max_value)
            BST(root.right, max_value)
        
        BST(root, float('-inf'))
        
        return self.res
