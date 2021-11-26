class Solution:

    def __init__(self, nums: List[int]):
        self.start = copy.deepcopy(nums)
        self.nums = nums
        

    def reset(self) -> List[int]:
        return self.start
        

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums
