class Solution:
    def lengthLongestPath(self, input):
        # maxlen = 0
        # pathlen = {0: 0}
        # for line in input.splitlines():
        #     depth = line.count('\t')
        #     name = line.lstrip('\t')
        #     if '.' in name:
        #         maxlen = max(maxlen, pathlen[depth] + len(name))
        #     else:
        #         pathlen[depth + 1] = pathlen[depth] + len(name) + 1  # +1 is "/"
        # return maxlen
        
        maxlen = 0
        pathlen = {0:0}
        
        for line in input.split('\n'):
            
            depth = line.count('\t')
            name = line[depth:]
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen
