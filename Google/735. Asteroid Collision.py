class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        ans = []
        
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                # ruin ans[-1], continue comparison
                if ans[-1] < -new:
                    ans.pop()
                # ruin both ans[-1] and new, pop ans[-1] and do not need to as new into ans, stop the comparison
                elif ans[-1] == -new:
                    ans.pop()
                    break
                # ruin new, stop the comparison
                else:
                    break
            else:
                ans.append(new)
        return ans
