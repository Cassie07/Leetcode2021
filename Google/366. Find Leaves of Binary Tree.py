class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.dic = collections.defaultdict(list)
        
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            cur_level = max(left, right) + 1
            self.dic[cur_level].append(root.val)
            return cur_level
        helper(root)
        return [i for i in self.dic.values()]
