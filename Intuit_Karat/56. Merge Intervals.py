class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        
        res = []
        tmp = intervals[0]
        
        for i in range(1,len(intervals)):
            
            if tmp[1] >= intervals[i][0]:
                tmp[1] = max(intervals[i][1], tmp[1])
            else:
                res.append(tmp)
                tmp = intervals[i]
        
        res.append(tmp)
        return res
