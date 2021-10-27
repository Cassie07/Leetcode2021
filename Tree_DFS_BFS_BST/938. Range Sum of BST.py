class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.sum = 0
        self.low, self.high = low, high
        
        def traversal(root):
            
            if not root:
                return
            
            if self.low <= root.val <= self.high:
                self.sum += root.val
                
            
            traversal(root.left)
            traversal(root.right)
        
        traversal(root)
        return self.sum
