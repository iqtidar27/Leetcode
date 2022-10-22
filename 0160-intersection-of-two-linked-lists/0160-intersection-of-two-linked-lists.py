# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #TC: O(m+n)
        #Constant Space
        pA = headA
        pB = headB
        lenA = 1
        lenB = 1
        
        while pA:
            pA = pA.next
            lenA += 1
        
        while pB:
            pB = pB.next
            lenB += 1
        
        pA = headA
        pB = headB
        
        if lenA > lenB:
            for i in range(lenA - lenB):
                pA = pA.next
        else:
            for i in range(lenB - lenA):
                pB = pB.next
        
        while pA != pB:
            pA = pA.next
            pB = pB.next
        
        return pB
