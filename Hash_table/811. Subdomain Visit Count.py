class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        hash_dict = {}
        
        for cpdomain in cpdomains:
            
            digit = cpdomain.split(' ')[0]
            domain = cpdomain.split(' ')[1]
            
            domain_list = domain.split('.')
            
            for i in range(len(domain_list)):
                tmp = domain_list[i:]
                
                sub_domain = ''
                for index, j in enumerate(tmp):
                    if index != len(tmp) -1:
                        sub_domain += j
                        sub_domain += '.'
                    else:
                        sub_domain += j
                
                if sub_domain in hash_dict.keys():
                    hash_dict[sub_domain] += int(digit)
                else:
                    hash_dict[sub_domain] = int(digit)
        
        res = []
        for domain, digit in hash_dict.items():
            res.append('{} {}'.format(digit, domain))
        
        return res
