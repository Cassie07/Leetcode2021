class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(l,h):
            
            if l < h:
                
                mid = l + (h - l) //2
                
                if target in matrix[mid]:
                    return True
                
                if target < matrix[mid][0]:
                    return binary_search(l,mid)
                elif target > matrix[mid][-1]:
                    return binary_search(mid + 1,h)
      
            else:
                return False
            
        return binary_search(0, len(matrix))
