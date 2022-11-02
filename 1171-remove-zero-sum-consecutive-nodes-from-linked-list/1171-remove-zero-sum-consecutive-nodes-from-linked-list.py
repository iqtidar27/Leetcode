# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #TC: O(N)
        #SC: O(N)
        if head is None:
            return None

        m = {}
        dummy = ListNode(0)
        dummy.next=head
        m = {0:dummy}
        prefixsum = 0
        while head is not None:
            prefixsum+=head.val
            if prefixsum in m:
                start = m[prefixsum]
                sumset = prefixsum
                while start is not None and start != head:
                    start = start.next
                    sumset +=start.val
                    if start != head:
                        m.pop(sumset)


                m[prefixsum].next=head.next

            else:
                m[prefixsum]=head

            head = head.next

        return dummy.next


