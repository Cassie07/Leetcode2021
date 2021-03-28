# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #print(TreeNode(preorder[0]))
        
        # change list to queue
        self.preorder = deque(preorder)
        self.map_inorder = {val:i for i,val in enumerate(inorder)}
        return self.recurs(0, len(preorder) - 1)
    
    def recurs(self, low, high):
        if low > high:
            return None
        
        # Queue: FIFO
        x = TreeNode(self.preorder.popleft())
        mid = self.map_inorder[x.val]
        
        # pre-order: mid --> left --> right
        # popleft(FIFO): mid --> left --> right
        x.left = self.recurs(low, mid - 1)
        x.right = self.recurs(mid + 1, high)
        return x
