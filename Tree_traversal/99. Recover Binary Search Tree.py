class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        cur, prev, drop, stack = root, TreeNode(float('-inf')), [], []
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
                
            node = stack.pop()

            if node.val < prev.val: drop.append((prev, node))
            prev, cur = node, node.right
            
        drop[0][0].val, drop[-1][1].val =  drop[-1][1].val, drop[0][0].val
        
