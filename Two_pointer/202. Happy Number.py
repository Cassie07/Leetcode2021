class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(num):
            total_sum = 0
            
            num = str(num)
            
            for i in num:
                total_sum += int(i)**2
                
            return total_sum
        
        slow = n
        fast = get_next(n)
        
        while fast != 1 and slow != fast:
            
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            
        return fast == 1
