class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        
        def helper(root, path_string):
            
            if not root:
                return
            
            if len(path_string) == 0:
                path_string = path_string + str(root.val)
            else:
                path_string = path_string + '->' + str(root.val)
            
            if not root.left and not root.right:
                self.res.append(path_string)
            
            helper(root.left, path_string)
            helper(root.right, path_string)
            
        self.res = []
        helper(root, '')

        return self.res
