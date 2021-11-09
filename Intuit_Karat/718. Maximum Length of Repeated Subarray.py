# bottom-up: better solution
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        dp =[[0] * (len(nums2) + 1) for i in range(len(nums1) + 1)]
        

            
        for i in reversed(range(len(nums1))):
            for j in reversed(range(len(nums2))):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1

        return max(max(item) for item in dp)

# top-bottom
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        dp =[[0] * (len(nums2) + 1) for i in range(len(nums1) + 1)]
        

            
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

        return max(max(item) for item in dp)
