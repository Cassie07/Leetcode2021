class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        
        cur = s[0]
        res = []
        tmp = 1
        for i in s[1:]:
            if i == cur:
                tmp += 1
            else:
                res.append(tmp)
                tmp = 1
                cur = i
        res.append(tmp)
        
        r = 0
        for i in range(len(res)-1):
            r += min(res[i], res[i+1])
            
