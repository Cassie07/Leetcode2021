class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        res = []
        for i in range(1, n+1):
            if n % i == 0:
                res.append(i)
 
        res.sort()
        
        return res[k-1] if k <= len(res) else -1
