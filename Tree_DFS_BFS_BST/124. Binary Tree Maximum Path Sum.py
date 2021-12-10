class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max = float('-inf')
        
        def helper(root):

            if not root:
                return 0
            
            left = max(helper(root.left),0)
            right = max(helper(root.right),0)
            self.max = max(self.max, left + right + root.val)

            return root.val + max(left, right)
        
        helper(root)
        return self.max
