class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def binary_search(low, high, piles, h):
            

            if low <= high:
                
                mid = low + (high - low) //2
                
                def count_hour(mid, piles, h):
                    
                    count = 0
                    
                    for pile in piles:
                        count += pile // mid
                        if pile % mid != 0:
                            count += 1
                    return count
                
                if count_hour(mid, piles, h) <= h:
                    return binary_search(low, mid - 1, piles, h)

                else:
                    return binary_search(mid + 1, high, piles, h)
            else:
                return low
        
        return binary_search(1, max(piles), piles, h)
