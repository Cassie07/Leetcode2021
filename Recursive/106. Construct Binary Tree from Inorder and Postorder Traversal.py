# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.postorder = postorder
        self.map_inorder = {val:i for i, val in enumerate(inorder)}

        return self.recur(0,len(inorder) - 1)
    
    def recur(self, low, high):
        if low > high:
            return None
        
        x = TreeNode(self.postorder.pop())
        mid = self.map_inorder[x.val]
        
        # post-order.push(): left --> right --> miid
        # post-order.pop(): mid --> right --> left
        # so firstly, we calculate x.right. Secondly, we calcualte x.left
        x.right = self.recur(mid+1, high)
        x.left = self.recur(low, mid-1)
        
        return x
