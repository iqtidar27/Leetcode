# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(-1, head)
        odd_head = head
        even_head = head.next
        connection_to_even = even_head
        
        while odd_head.next and even_head.next:
            odd_head.next = odd_head.next.next
            odd_head = odd_head.next
            even_head.next = even_head.next.next
            even_head = even_head.next
        
        odd_head.next = connection_to_even
        
        return dummy.next