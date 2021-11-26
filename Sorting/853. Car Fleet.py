class Solution:
    #def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    def carFleet(self, target, pos, speed):
        time = [(target - p)/s for p,s in sorted(zip(pos, speed))]
        
        prev, res = 0,0
        for t in reversed(time):
            if t > prev:
                res += 1
                prev = t
        return res
