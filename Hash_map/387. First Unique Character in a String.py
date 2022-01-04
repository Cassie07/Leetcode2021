class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dictionary = {}
        
        for index,letter in enumerate(s):
            
            if letter in dictionary.keys():
                dictionary[letter][0] += 1
            else:
                dictionary[letter] = [1, index]
        
        res = float('inf')
        for value in dictionary.values():
            time, index = value[0],value[1]
            if time == 1 and index < res:
                res = index
        
        if res == float('inf'):
            return -1
        
        return res
