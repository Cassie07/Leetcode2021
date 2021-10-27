class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        v = []
        
        def dfs(root):
            
            if root:
                dfs(root.left)
                v.append(root)
                dfs(root.right)
        
        dfs(root)
        
        def balance(v):
            
            if not v:
                return None
            
            mid = len(v)//2
            
            root = v[mid]
            root.left = balance(v[:mid])
            root.right = balance(v[mid+1:])
            
            return root
        
        return balance(v)
