class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # recursion
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
