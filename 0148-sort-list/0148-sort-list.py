# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #TC: O(nlogn)
        #SC: O(logn)
        
        def findMid(node):
            
            slow = node
            fast = node.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def mergeList(l1, l2):
            dummy = ListNode(-1)
            curr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                
                curr = curr.next
                
            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2
                
            return dummy.next
        
        if not head or not head.next:
            return head
        
        left = head
        right = findMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        return mergeList(left, right)
        
        
        