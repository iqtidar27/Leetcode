# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #TC: O(N)
        #SC: O(N)
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        for i in range(1, left):
            prev = prev.next
            
        curr = prev.next
        
        for j in range(1, right - left + 1):
            future = curr.next
            curr.next = future.next
            future.next = prev.next
            prev.next = future
            
        return dummy.next
            