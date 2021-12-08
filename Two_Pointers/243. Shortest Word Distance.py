class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        word_dict = collections.defaultdict(list)
        
        for index, word in enumerate(wordsDict):
            word_dict[word].append(index)
            
        word1_pos = word_dict[word1]
        word2_pos = word_dict[word2]
        w1 = 0
        w2 = 0
        res = float('inf')
        
        while w1 < len(word1_pos) and w2 < len(word2_pos):
            
            res = min(res,abs(word1_pos[w1] - word2_pos[w2]))
            
            if word1_pos[w1] < word2_pos[w2]:
                w1 += 1
            else:
                w2 += 1

        return res
