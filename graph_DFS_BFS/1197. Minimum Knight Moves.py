class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        # the offsets in the eight directions
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),(-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        count = 0
        queue = deque([(0,0)])
        cur_x, cur_y = 0,0
        visited = set((0,0))
        
        while queue:
            cur_cnt = len(queue)
            for i in range(cur_cnt):
                cur_x, cur_y = queue.popleft()
                if (cur_x, cur_y) == (x,y):
                    return count
                
                for offsets_x, offsets_y in offsets:
                    next_x, next_y = cur_x + offsets_x, cur_y + offsets_y
                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))
            count += 1
        
        return count
