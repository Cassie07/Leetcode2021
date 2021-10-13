# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def Binary_search(low, high, nums):
            
            if low <= high:
                mid = low + (high - low) // 2

                x = TreeNode()
                x.val = nums[mid]
                x.left = Binary_search(low, mid - 1, nums)
                x.right = Binary_search(mid + 1, high, nums)
            
                return x
            else:
                return None
        
        return Binary_search(0, len(nums)-1, nums)
