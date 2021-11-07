
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        # Timsort : O(nlogn)
        intervals.sort()
        
        # O(n)
        for index in range(len(intervals)-1):
            
            interval1 = intervals[index]
            interval2 = intervals[index + 1]
            
            if interval1[1] > interval2[0]:
                return False
            
        # So the entire time complexity should O(nlogn + n) = O(nlogn)
        
        return True
