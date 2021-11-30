class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = set()#[]
        adj_dict = collections.defaultdict(list)
        
        for parent,child in edges:
            adj_dict[parent].append(child)
            adj_dict[child].append(parent)
    

        
        if n - 1 != (len(edges)): return False
            
        def have_cycle(cur, parent):
        
            visited.add(cur)
            
            children = adj_dict[cur]
            
            for child in children:
                if child not in visited:
                    if have_cycle(child, cur):
                        return True
                elif child != parent:
                    return True
            return False


        
        if n == 1: return True
        
        if have_cycle(0,-1):
            return False
        
        if len(visited) != n:
            return False
        else:
