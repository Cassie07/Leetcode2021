class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        res = collections.defaultdict(list)
        
        def dfs(root):
            if root:
                struct = '{},{},{}'.format(str(root.val), dfs(root.left), dfs(root.right))
                res[struct].append(root)
            else:
                return "null"
            return struct
        
        dfs(root)
        
        return [res[struct][0] for struct in res.keys() if len(res[struct]) > 1]
