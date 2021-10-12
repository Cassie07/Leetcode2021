class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        
        # Recursive
        def binary_search(low, high, arr, target):
            
            if low <= high:

                mid = low + (high-low)//2

                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    return binary_search(mid + 1, high, arr, target)
                else:
                    return binary_search(low, mid - 1, arr, target)
            else:
                return low
        
        return binary_search(0, len(nums)-1, nums, target)
