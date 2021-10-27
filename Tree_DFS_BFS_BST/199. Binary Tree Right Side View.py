class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def dfs(root, layer):
            
            if not root:
                return
            
            if len(self.res) < layer:
                self.res.append(root.val)
            else:
                self.res[layer-1] = root.val
                
            letf = dfs(root.left, layer + 1)
            right = dfs(root.right, layer + 1)
            
        self.res = []
        dfs(root, 1)
        return self.res
