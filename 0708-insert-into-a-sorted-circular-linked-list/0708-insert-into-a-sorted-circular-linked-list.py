"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        curr = head
        while True:
            if curr.val <= insertVal <= curr.next.val:
                break
            elif curr.next == head:
                break
            elif curr.val > curr.next.val:
                if curr.val <= insertVal:
                    break
                if curr.next.val >= insertVal:
                    break
            curr = curr.next
            
        node = Node(insertVal)
        node.next = curr.next
        curr.next = node
        
        return head