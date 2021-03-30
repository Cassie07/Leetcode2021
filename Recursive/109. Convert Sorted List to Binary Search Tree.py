# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def binary_search(start):
            
            # start point is empty
            if not start:
                return None
            
            # start point is the only element in list
            if not start.next:
                return TreeNode(start.val)
            
            # Save for x.left
            save = start
            
            # find mid point in a linked list
            slow = start
            fast = start.next.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next  
            mid = slow.next
            
            # Cut off the left sub-tree, otherwise the code will continue forever
            slow.next = None
            
            # update root and its left/right node
            x = TreeNode(mid.val)
            x.left = binary_search(save)
            x.right = binary_search(mid.next)
            return x
        
        return binary_search(head)
