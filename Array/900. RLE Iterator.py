class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.map = encoding
        self.i = 0
        # for i in range(len(encoding)//2):
        #     for j in range(encoding[2*i]):
        #         self.map.append(encoding[2*i+1])


    def next(self, n: int) -> int:

        while self.i < len(self.map):
            time = self.map[self.i]
            if n <= time:
                self.map[self.i] -= n
                return self.map[self.i + 1]
            else:
                n -= self.map[self.i]
                self.i += 2
        return -1
