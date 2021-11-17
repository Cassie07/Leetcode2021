class Solution(object):
    def canReorderDoubled(self, A):
        
        # O(n)
        count = collections.Counter(A)
        
        # O(nlogn) + O(n) = O(NlogN)
        for x in sorted(A, key = abs):

            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True
