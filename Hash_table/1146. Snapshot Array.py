class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[-1, 0]] for i in range(length)]
        self.snap_time = 0

        

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snap_time, val])

    def snap(self) -> int:
        self.snap_time += 1 
        return self.snap_time - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.array[index], [snap_id, float('inf')]) - 1
        return self.array[index][i][1]
