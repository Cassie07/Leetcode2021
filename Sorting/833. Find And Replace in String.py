class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        add = []
        last = -1
        
        # [4,6,1]: sort indices to an ordered list
        # update other lists
        # O(nlogn)
        sorted_indices = sorted((e,i) for i,e in enumerate(indices))
        sources = [sources[i[1]] for i in sorted_indices]
        indices = [indices[i[1]] for i in sorted_indices]
        targets = [targets[i[1]] for i in sorted_indices]
        
        # Found the start position for replacing
        # O(n)
        for index in range(len(indices)):
            indice = indices[index]
            source = sources[index]
            target = targets[index]
            
            if source in s[indice:indice + len(source)] and last < indice:
                add.append(index)
                last = indice + len(source) -1
                
        # if len(add) == 0, means no target need to be replace
        if len(add) == 0: return s
        else:
            last = -1
            res = ''
            # replace, keep the string between last and the next indices
            # add replace in string
            # O(n)
            for index,i in enumerate(add):
                start = indices[i]

                if last != -1:
                    res += s[last: indices[i]]
                elif last == -1 and indices[i] != 0:
                    res += s[0:indices[i]]
                res += targets[i]
                last = start + len(sources[i])

            res += s[last:]
            return res
            
