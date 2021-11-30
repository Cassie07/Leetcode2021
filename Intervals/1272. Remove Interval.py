class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        # to be remove :[r1,r2] r1 <=x < r2
        # array [a,b]
        
        res = []
        r1, r2 = toBeRemoved
        for interval in intervals:
            
            start, end = interval
            
            
            
            if start < r1:
                res.append([start, min(r1,end)])
            if end > r2:
                res.append([max(start, r2), end])
            
        return res
