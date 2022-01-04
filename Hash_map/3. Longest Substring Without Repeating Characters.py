class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = 0
        
        for index_start in range(len(s)):
            repeat = [s[index_start]]
            for index_next in range(index_start + 1, len(s)):
                if s[index_next] not in repeat:
                    repeat.append(s[index_next])
                else:
                    break
            if length < len(repeat):
                length = len(repeat)
        
        return length
