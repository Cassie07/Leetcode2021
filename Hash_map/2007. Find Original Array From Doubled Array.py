class Solution:

    
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        count = collections.Counter(changed)
        
        
        ori = []
        
        # if len(changed) == 1:
        #     return []

        if count[0] % 2:
            return []
        
        for i in sorted(changed, key = abs):

            if count[i] == 0: continue
            if count[i * 2] == 0: return []
            
            ori.append(i)
            count[i] -= 1
            count[i * 2] -= 1
        
        return ori
