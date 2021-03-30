# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def binary_search(low, high):
            if low > high:
                return None
            
            mid = (high - low)//2 + low
            x = TreeNode(nums[mid])
            
            x.left = binary_search(low, mid - 1)
            x.right = binary_search(mid + 1, high)
            
            return x
        return binary_search(0,len(nums) - 1)
