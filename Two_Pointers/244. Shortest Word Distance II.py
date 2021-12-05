class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_pos_dict = collections.defaultdict(list)
        for pos, word in enumerate(wordsDict):
            self.word_pos_dict[word].append(pos)
            
        

    def shortest(self, word1: str, word2: str) -> int:
        word1_list = self.word_pos_dict[word1]
        word2_list = self.word_pos_dict[word2]
        
        res = float('inf')
        
        # Brute force: O(N)
        # for i in word1_list:
        #     for j in word2_list:
        #         tmp = abs(i-j)
        #         if res > tmp:
        #             res = tmp
        
        l1,l2 = 0,0
        
        # O(N)
        while l1 < len(word1_list) and l2 < len(word2_list):
            res = min(res, abs(word1_list[l1] - word2_list[l2]))
            
            if word1_list[l1] < word2_list[l2]:
                l1 += 1
            else:
                l2 += 1
                
        return res
