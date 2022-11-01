# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Two pass algorithm
        
        p = head
        length = 1
        
        for i in range(k-1):
            p = p.next
            length += 1
        
        q = p.next
        
        while q:
            q = q.next
            length += 1
        
        r = head
        
        for i in range(length - k):
            r = r.next
            
        p.val, r.val = r.val, p.val
        
        return head