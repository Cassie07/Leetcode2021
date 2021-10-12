class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def upper_round (num,divisor):
            count = 0
            
            count += num // divisor
            if num % divisor != 0:
                count += 1
            return count
        
        def binary_search(low, high, nums, threshold):
            
            if low <= high:
                
                mid = low + (high - low)//2
                
                def helper(mid, nums, threshold):
                    count = 0
                    
                    for num in nums:
                        count += upper_round(num, mid)
                    
                    return count
                
                if helper(mid, nums, threshold) <= threshold:
                    return binary_search(low, mid - 1, nums, threshold)
                else:
                    return binary_search(mid + 1, high, nums, threshold)
            else:
                return low
            
        return binary_search(1, max(nums), nums, threshold)
