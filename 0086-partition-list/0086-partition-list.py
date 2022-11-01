# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = less_head = ListNode(-1)
        greater = greater_head = ListNode(-1)
        
        while head:
            if head.val < x:
                less_head.next = head
                less_head = less_head.next
            else:
                greater_head.next = head
                greater_head = greater_head.next
                
            head = head.next
        
        less_head.next = greater.next
        greater_head.next = None
        
        return less.next