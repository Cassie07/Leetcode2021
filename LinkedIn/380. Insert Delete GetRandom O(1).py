class RandomizedSet:

    def __init__(self):
        self.res = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.res:
            self.res[val] = len(self.list)
            self.list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.res:
            self.res[self.list[-1]] = self.res[val] 
            self.list[-1], self.list[self.res[val]] = self.list[self.res[val]], self.list[-1]
            self.list.pop()
            del self.res[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        num = random.randint(0,len(self.list)-1)
        return self.list[num]
