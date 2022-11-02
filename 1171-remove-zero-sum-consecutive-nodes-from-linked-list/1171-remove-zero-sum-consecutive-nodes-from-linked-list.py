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
        m[0]=dummy
        prefixsum = 0
        while head is not None:
            prefixsum+=head.val
            if prefixsum in m.keys():
                start = m[prefixsum]
                sum = prefixsum
                while start is not None and start is not head:
                    start = start.next
                    sum+=start.val
                    if start is not head:
                        m.pop(sum)


                m[prefixsum].next=head.next

            else:
                m[prefixsum]=head

            head = head.next

        return dummy.next


