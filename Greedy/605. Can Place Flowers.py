class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        index = 0
        
        count = 0
        for index in range(len(flowerbed)):

            if flowerbed[index] == 0 and (index == 0 or flowerbed[index - 1] == 0) and (index == len(flowerbed)-1 or flowerbed[index + 1] == 0):
                flowerbed[index] = 1
                count +=1
            if count >= n:
                return True
        return False
        
