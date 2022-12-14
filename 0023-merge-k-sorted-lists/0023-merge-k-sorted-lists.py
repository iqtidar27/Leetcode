# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        
        for single_list in lists:
            while single_list:
                minHeap.append(single_list.val)
                single_list = single_list.next
        
        heapq.heapify(minHeap)
        dummy = ListNode(-1)
        head = dummy
        while minHeap:
            head.next = ListNode(heapq.heappop(minHeap))
            head = head.next
        
        return dummy.next
        '''
        #O(nlogK)
        def mergeList(list1, list2):
            dummy = ListNode(-1)
            curr = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next

            if list1:
                curr.next = list1
            elif list2:
                curr.next = list2

            return dummy.next
        
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedList.append(mergeList(l1, l2))
            lists = mergedList
        
        return lists[0]
                
        '''
        