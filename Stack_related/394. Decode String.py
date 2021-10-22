class Solution:
    def decodeString(self, s: str) -> str:
        
        stack, cur_num, cur_string = [], 0, ''
        
        for letter in s:
            
            if letter.isdigit():
                cur_num = 10 * cur_num + int(letter)
                
            elif letter == '[':
                stack.append(cur_string)
                stack.append(cur_num)
                cur_num, cur_string = 0 , ''
                
            elif letter == ']':
                num = stack.pop()
                pre_string = stack.pop()
                cur_string = pre_string + num * cur_string
                
            else:
                cur_string += letter
                
        return cur_string
