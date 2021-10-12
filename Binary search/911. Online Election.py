class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.memo = [0 for i in range(max(self.persons)+1)]
        self.lead = []
        leader = 0
        leader_index= 0

        for i in self.persons:
            self.memo[i] += 1
            
            # test equal
            if self.memo[i] >= leader:
                self.lead.append(i)
                leader = self.memo[i]
                leader_index = i

            else:
                self.lead.append(leader_index)


        print(self.lead)


    def q(self, t: int) -> int:
        
        def binary_search(low, high, arr, t):
            
            if low <= high:
                
                mid = low + (high - low) // 2
                
                if arr[mid] <= t:
                    return binary_search(mid + 1, high, arr, t)
                else:
                    return binary_search(low, mid-1, arr, t)
            else:
                return high
        
        index = binary_search(0, len(self.times)-1, self.times, t)
        
        return self.lead[index]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
