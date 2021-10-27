class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
            self.conn = collections.defaultdict(list)
            
            def connection(parent, child):
                
                if parent and child:
                    self.conn[parent.val].append(child.val)
                    self.conn[child.val].append(parent.val)
                    
                if child.left: connection(child, child.left)
                if child.right: connection(child, child.right)
                    
            connection(None, root)
            
            bfs = [target.val]
            seen = set(bfs)
            
            for i in range(k):

                # find nodes in the i-hop of target (expand hop by looping) 
                new = []
                for node in bfs:
                    for connect_node in self.conn[node]:
                        if connect_node not in seen:
                            new.append(connect_node)
                    
                bfs = new
                seen |= set(bfs)
                
            return bfs
