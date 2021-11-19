class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        word_dict = collections.defaultdict(list)
        

        for word in words:
            word_dict[word[0]].append(word)
            
        count = 0
        

        for char in s:
            expect_w = word_dict[char]
            word_dict[char] = []
            
            for i in expect_w:
                if len(i) == 1:
                    count += 1
                else:
                    word_dict[i[1]].append(i[1:])
                    
        return count
