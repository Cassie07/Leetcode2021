class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def dfs(root, path):
            
            if not root:
                return
            if not root.left and not root.right:
                path = path * 10 + root.val
                self.res += path
            
            dfs(root.left, path*10 + root.val)
            dfs(root.right, path*10 + root.val)
               
        
        self.res = 0
        dfs(root, 0)
        return self.res
