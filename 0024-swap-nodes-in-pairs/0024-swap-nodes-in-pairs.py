# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(-1, head)
        prev = dummy
        
        while head and head.next:
            first = head
            second = head.next
            first.next = second.next
            second.next = first
            prev.next = second
            
            prev = first
            head = first.next
            
        return dummy.next