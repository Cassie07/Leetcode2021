class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def helper(time_string):
            
            hrs, mins = time_string.split(':')[0], time_string.split(':')[1]
            
            return int(hrs) * 60 + int(mins)
        
        hash_dict = {}
        
        for name, time_string in zip(keyName, keyTime):
            if name in hash_dict:
                hash_dict[name].append(helper(time_string))
            else:
                hash_dict[name] = [helper(time_string)]
                

        res = []
        
        for name, times in hash_dict.items():
            
            max_repeat = 0
            times.sort()
            

            for time in range(len(times)):
                
                repeat = 1
                
                   
                diff = [times[i] - times[time] for i in range(time + 1,len(times))]
                
                
                for i in diff: 
                    if 0<= i <= 60: repeat += 1
                max_repeat = max(max_repeat, repeat)
            
            if max_repeat >= 3:
                res.append(name)
                    
        res.sort()           
        return res
