"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        hash_start = {}
        res = []
        
        for employee in schedule:
            for time in employee:
                if time.start not in hash_start.keys():
                    hash_start[time.start] = time
                else:
                    hash_start[time.start].end = max(hash_start[time.start].end, time.end)
        
        merge_list = [[i.start, i.end] for i in hash_start.values()]
        merge_list.sort()
        
        new_merge = []
        tmp_interval = []
        for index in range(len(merge_list)-1):
            interval1 = merge_list[index]
            interval2 = merge_list[index + 1]

            if interval1[1] < interval2[0]:
                new_merge.append(interval1)
            else:
                tmp_interval = [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
                merge_list[index + 1] = tmp_interval
                
        new_merge.append(merge_list[len(merge_list)-1])

        
        for index in range(len(new_merge) - 1):
            tmp = Interval()
            tmp.start = new_merge[index][1]
            tmp.end = new_merge[index + 1][0]
            res.append(tmp)
        return res

    
