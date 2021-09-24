class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        def modified_BinarySearch(low, high, arr):
            if low == high:
                return arr[low]
            
            if low < high:
                
                mid = 2*((low + high) //4)
                
                if arr[mid] == arr[mid+1]:
                    return modified_BinarySearch(mid+2, high, arr)
                else:
                    return modified_BinarySearch(low, mid, arr)
            
        return modified_BinarySearch(0, len(nums)-1, nums)
