class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        for i in reversed(sorted(nums)):
            k -= 1
            if k == 0:
                return i
