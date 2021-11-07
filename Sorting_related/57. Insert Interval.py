class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        
        if not intervals:
            return [newInterval]
        
        for index, i in enumerate(intervals):
            
            if newInterval[1] < i[0]:
                res.append(newInterval)
                return res + intervals[index:]
                
            if newInterval[0] > i[1]:
                res.append(i)
            else:
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
                
        res.append(newInterval)
        return res
