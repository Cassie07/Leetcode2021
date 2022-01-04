class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        

        dictionary = {i-97: chr(i).upper() for i in range(97,123)}
        remainder = 1
        res = ''
        
        while columnNumber > 26:
            
            remainder = (columnNumber-1) % 26
            res += dictionary[remainder]
            columnNumber = (columnNumber-1) // 26
        
        else:
            res += dictionary[columnNumber-1]
        return res[::-1]
