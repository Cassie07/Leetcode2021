class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict1 = {}
        
        for i in s:
            if i in dict1.keys():
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for i in t:
            if i in dict1.keys():
                dict1[i] -= 1
            else:
                return False
            
        for i in dict1.values():
            if i != 0:
                return False
        
        return True
