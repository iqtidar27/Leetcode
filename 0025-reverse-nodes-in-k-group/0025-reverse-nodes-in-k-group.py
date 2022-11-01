# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #TC: O(N)
        #SC: O(1)
        
        def getKth(curr, k):
            
            while k > 0 and curr:
                curr = curr.next
                k -= 1
            
            return curr
        
        dummy = ListNode(-1, head)
        groupPrev = dummy
        
        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev = groupNext
            curr = groupPrev.next
            
            while curr != groupNext:
                Next = curr.next
                curr.next = prev
                prev = curr
                curr = Next
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next
    