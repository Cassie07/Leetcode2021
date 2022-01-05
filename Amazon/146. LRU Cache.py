class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur_cap = 0
        self.save = collections.OrderedDict()


    def get(self, key: int) -> int:
        if key in self.save.keys():
            v = self.save.pop(key)
            self.save[key] = v
            return v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.save:
            self.save.pop(key)
            self.cur_cap -= 1
     
        else:
            if self.capacity == self.cur_cap:
                self.save.popitem(last = False)
                self.cur_cap -= 1
        
        self.save[key] = value
        self.cur_cap += 1
