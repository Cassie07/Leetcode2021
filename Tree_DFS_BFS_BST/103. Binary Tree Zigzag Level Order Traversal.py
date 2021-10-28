# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        res, parent, child = [], [root],[]
        
        flag = 0
        stop = True
        while stop:
            res.append([i.val for i in parent])
            while parent:

                node = parent.pop()
                
                if flag == 0:
                    if node.right: child.append(node.right)
                    if node.left: child.append(node.left)
                else:
                    if node.left: child.append(node.left)
                    if node.right: child.append(node.right)

            if flag == 0:
                flag = 1
            else:
                flag = 0
                
            if len(child) == 0:
                stop = False
            parent = [i for i in child]
            child = []
        
        return res
        
