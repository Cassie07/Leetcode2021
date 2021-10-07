# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
# iteration        
#         low, high = 1, n
        
#         while (low <= high):
#             mid = low + (high - low)//2
                
#             flag = guess(mid)
#             print((mid,flag))

#             if flag == 0:
#                 print(mid)
#                 return mid

#             elif flag == -1:
#                 high = mid - 1

#             else:
#                 low = mid + 1

# recursion
        def binary(low, high):
            
                
            mid = low + (high - low)//2

            flag = guess(mid)
            print((mid,flag))

            if flag == 0:
                print(mid)
                return mid

            elif flag == -1:
                return binary(low, mid - 1)

            else:
                return binary(mid + 1, high)

        return binary(1, n)
