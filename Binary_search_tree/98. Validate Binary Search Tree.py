class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        
        
        def helper(root, bound_min, bound_max):
            
            if not root:
                return True
            
            if not helper(root.left, bound_min, root.val):
                return False
            

            if not bound_min < root.val < bound_max:
                return False
            
            if not helper(root.right, root.val, bound_max):
                return False
            
            return True
        
        return helper(root, float("-inf"), float("inf"))
