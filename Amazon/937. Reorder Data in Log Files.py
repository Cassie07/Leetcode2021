class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digit = []
        letter = []
        letter_dic = collections.defaultdict(list)
        
        for i in logs:
            words = i.split(' ')
            if words[1].isdigit():
                digit.append(i)
            else:
                string = ''
                for w in words[1:]:
                    string += w + ' '
                letter_dic[string].append(words[0])

        content = list(letter_dic.keys())
        content.sort()
        
        for i in content:
            
            for j in sorted(list(letter_dic[i])):
                string = j + ' ' + i
                letter.append(string[:-1])
        
        return letter + digit
