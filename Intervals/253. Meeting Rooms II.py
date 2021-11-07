class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        heap = []
        
        for i in intervals:
            
            if heap and i[0] >= heap[0]:
                heapreplace(heap, i[1])
            else:
                heappush(heap, i[1])
        
        return len(heap)
        

        
