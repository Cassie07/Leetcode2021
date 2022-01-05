class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()

            if stones[-1] == stones[-2]:
                stones = stones[:-2]
            else:
                a = stones.pop()
                b = stones.pop()
                stones.append(abs(a - b))
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
