class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_dic = {i:index for index,i in enumerate(order)}
        
        
        if len(words) == 1:
            return True
        
        res = []
        for index in range(len(words)-1):
            
            word1 = words[index]
            word2 = words[index + 1]
            print((word1, word2))
            
            for letter in range(max(len(word1), len(word2))):
                
                if letter >= len(word1):
                    res.append('true')
                    break
                else:
                    i = word1[letter]
                    
                if letter>= len(word2):
                    res.append('false')
                    break
                else:
                    j = word2[letter]
                    
                if i == j:
                    continue
                else:
                    order_i = order_dic[i]
                    order_j = order_dic[j]
                    
                    print((i,j))
                    if order_i > order_j:
                        res.append('false')
                        break
                    else:
                        res.append('true')
                        break
            if 'false' in res: return False
        return True
