class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        if not root: return False
        
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# much faster one: 28s
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def helper(root, target):
            if root:
                
                if not root.left and not root.right and root.val == target:
                    return True
                
                return helper(root.left, target - root.val) or helper (root.right, target - root.val)
            else:
                return False
            
        return helper(root, targetSum)
