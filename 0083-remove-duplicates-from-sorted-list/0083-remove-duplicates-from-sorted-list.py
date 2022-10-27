# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        dummy = ListNode(-1, head)
        curr = head
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
            
        return dummy.next