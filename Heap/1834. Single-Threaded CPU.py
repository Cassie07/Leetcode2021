class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        enque_process_list = sorted([(i[0], i[1],index) for index, i in enumerate(tasks)])
        
        # for index,i in enumerate(tasks):
        #     enque_process_dict[i[0]].append((i[1], index))
        # print(enque_process_dict)
            
        res = []
        wait = []
        i = 0
        time = enque_process_list[0][0]
        while len(res) < len(enque_process_list):
            while i < len(enque_process_list) and enque_process_list[i][0] <= time:
                heapq.heappush(wait, (enque_process_list[i][1], enque_process_list[i][2]))
                i += 1
            if wait:
                current = heapq.heappop(wait)
                res.append(current[1])
                time += current[0]  
            elif i < len(enque_process_list):
                time = enque_process_list[i][0]
            
        return res
