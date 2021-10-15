# Recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        self.res = []
        if not root:
            return []
        
        def helper(root):
            
            if root.left:
                helper(root.left)
            
            self.res.append(root.val)
            
            if root.right:
                helper(root.right)
        
        helper (root)
        
        return self.res

# iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack, res = [],[]
        
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            if not stack:
            # if len(stack) == 0:
                return res
            
            node = stack.pop()
            res.append(node.val)
            root = node.right
