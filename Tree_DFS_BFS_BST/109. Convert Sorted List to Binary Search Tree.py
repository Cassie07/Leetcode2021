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
        
        def Find_mid(start):
            
            slow = start
            fast = slow.next.next
            
            while fast and fast.next:
                
                slow = slow.next
                fast = fast.next.next
                
            return slow, slow.next
        
        def Binary_search(start):
            
            # empty
            if start is None:
                return None
            
            # single item
            if start.next is None:
                return TreeNode(start.val)
            
            pre_mid, mid = Find_mid(start)
            
            x = TreeNode()
            x.val = mid.val
            
            # cut-off the linked list
            pre_mid.next = None

            x.left = Binary_search(start)
            x.right = Binary_search(mid.next)
            return x
        
        return Binary_search(head)# Definition for singly-linked list.
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
        
        def Find_mid(start):
            
            slow = start
            fast = slow.next.next
            
            while fast and fast.next:
                
                slow = slow.next
                fast = fast.next.next
                
            return slow, slow.next
        
        def Binary_search(start):
            
            # empty
            if start is None:
                return None
            
            # single item
            if start.next is None:
                return TreeNode(start.val)
            
            pre_mid, mid = Find_mid(start)
            
            x = TreeNode()
            x.val = mid.val
            
            # cut-off the linked list
            pre_mid.next = None

            x.left = Binary_search(start)
            x.right = Binary_search(mid.next)
            return x
        
        return Binary_search(head)
