# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        if not root:
            return []

        if root.left == None and root.right == None and root.val == targetSum:
            return [[root.val]]
        
        # [[a]] + [[b]] = [[a,b]]
        # [[a]] + [] [[a]]
        targetSum -= root.val
        ret = self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
            
        
        return [[root.val] + i for i in ret]
