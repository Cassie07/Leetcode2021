class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        res = 0
        for i,j in zip(sorted(nums), sorted(nums)[::-1]):
            res = max(res, i+j)
            
        return res
