"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        self.important_score = 0
        
        # O(N)
        self.dic_employee = {employee.id:[employee.importance,employee.subordinates] for employee in employees}
        
        # O(N)
        def dfs(root_id):
            
            self.important_score += self.dic_employee[root_id][0]
            
            if len(self.dic_employee[root_id][1]) != 0:
                for sub in self.dic_employee[root_id][1]:
                    dfs(sub)
        dfs(id)
        
        return self.important_score
