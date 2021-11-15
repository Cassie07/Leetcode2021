class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic.keys():
            self.dic[key] = [(value, timestamp)]
        else:
            self.dic[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dic.keys():
            l,r = 0, len(self.dic[key])
            while l < r:

                mid = l + (r-l) // 2

                if timestamp < self.dic[key][mid][1]:
                    r = mid
                else:
                    l = mid + 1

            if r == 0: return ''
            else: return self.dic[key][r-1][0]
        return ''
