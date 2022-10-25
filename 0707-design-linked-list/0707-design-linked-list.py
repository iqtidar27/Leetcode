#Doubly Linked List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
        
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        if index < self.size - index:
            curr = self.head
            for i in range(index+1):
                curr = curr.next
            return curr.val
        else:
            curr= self.tail
            for i in range(self.size - index):
                curr = curr.prev
                
            return curr.val

    def addAtHead(self, val: int) -> None:
        pred = self.head
        succ = self.head.next
        to_add = ListNode(val)
        self.size += 1
        to_add.next = succ
        to_add.prev = pred
        pred.next = to_add
        succ.prev = to_add

    def addAtTail(self, val: int) -> None:
        succ = self.tail
        pred = self.tail.prev
        to_add = ListNode(val)
        self.size += 1
        to_add.next = succ
        to_add.prev = pred
        pred.next = to_add
        succ.prev = to_add

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            if index < self.size - index:
                curr = self.head
                for i in range(index):
                    curr = curr.next
                pred = curr
                succ = curr.next
                to_add = ListNode(val)
                self.size += 1
                to_add.next = succ
                to_add.prev = pred
                pred.next = to_add
                succ.prev = to_add
            else:
                curr = self.tail
                for i in range(self.size - index):
                    curr = curr.prev
                succ = curr
                pred = curr.prev
                to_add = ListNode(val)
                self.size += 1
                to_add.next = succ
                to_add.prev = pred
                pred.next = to_add
                succ.prev = to_add
                
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index < self.size - index:
            curr = self.head
            for i in range(index):
                curr = curr.next
            pred = curr
            succ = curr.next.next
            pred.next = succ
            succ.prev = pred
            self.size -= 1
        else:
            curr = self.tail
            for i in range(self.size - index - 1):
                curr = curr.prev
                
            succ = curr
            pred = curr.prev.prev
            succ.prev = pred
            pred.next = succ
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
'''
#singly Linked List
def __init__(self, x):
        self.val = x
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(-1)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for i in range(index + 1):
            curr = curr.next
            
        return curr.val

    def addAtHead(self, val: int) -> None:
        curr = self.head
        to_add = ListNode(val)
        self.size += 1
        to_add.next = curr.next
        curr.next = to_add

    def addAtTail(self, val: int) -> None:
        curr = self.head
        
        for i in range(self.size):
            curr = curr.next
        
        to_add = ListNode(val)
        self.size += 1
        to_add.next = curr.next
        curr.next = to_add

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            to_add = ListNode(val)
            self.size += 1
            to_add.next = curr.next
            curr.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        curr = self.head
        for i in range(index):
            curr = curr.next
        
        self.size -= 1
        curr.next = curr.next.next
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
'''
