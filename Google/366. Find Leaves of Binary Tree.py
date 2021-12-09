class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.dic = {}
        
        def dfs(root):
            
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            level = max(left,right) + 1
            if level not in self.dic.keys():
                self.dic[level] = [root.val]
            else:
                self.dic[level].append(root.val)
            return level
        
        dfs(root)
        
        res = [i for i in self.dic.values()]
        return res
