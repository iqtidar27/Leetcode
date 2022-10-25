# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        1.find the length
        2. k = k%length
            if k == 0:
                return head
        3. else. start from head
        4. run a loop length - k -1 = 2
        5. newhead = curr.next
        6. curr.next = none
        7. tail.next = head
        
        '''
        if not head:
            return None
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        
        if k == 0:
            return head
        
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        
        newHead = curr.next
        tail.next = head
        curr.next = None
        
        return newHead
       