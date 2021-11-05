class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        string = 'abcdefghijklmnnopqrstuvwxyz'
        dictionary = {letter:index+1 for index,letter in enumerate(string)}
        
        dic_word = {}
        for word in strs:
            letters = []
            for letter in word:
                letters.append(letter)
            letters.sort()
            letters = tuple(letters)
            if letters in dic_word.keys():
                dic_word[letters].append(word)
            else:
                dic_word[letters] = [word]
        
        return [i for i in dic_word.values()]
