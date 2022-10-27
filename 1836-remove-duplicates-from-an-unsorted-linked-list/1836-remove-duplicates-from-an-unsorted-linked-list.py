# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        #Two pass solution
        if not head.next:
            return head
        
        dic = defaultdict(int)
        curr = head
        while curr:
            if curr.val not in dic:
                dic[curr.val] = 1
            else:
                dic[curr.val] += 1
            curr = curr.next
            
        dummy = ListNode(-1, head)
        curr = head
        prev = dummy
        #print(dic)
        
        while curr:
            if dic[curr.val] > 1:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        
        return dummy.next
        
        