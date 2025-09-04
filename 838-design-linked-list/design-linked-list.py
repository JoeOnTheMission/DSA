class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        # dummy node
        self.head = Node(0)
        self.tail = Node(0)
        # connect the dummy nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next#this lets me start at the real head of the linked list
        while cur and index > 0:# transverse the list until we get to index
            cur = cur.next
            index -= 1
        if cur and cur != self.tail and index == 0:#check if we found wt we needed
            return cur.value
        return -1
    def addAtHead(self, val: int) -> None:
        #4 pointers to be changed
        node,next,prev = Node(val), self.head.next,self.head
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        # 4 pointers to be changed
        node, next, prev = Node(val), self.tail, self.tail.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next  # this lets me start at the real head of the linked list
        while cur and index > 0:  # transverse the list until we get to index
            cur = cur.next
            index -= 1
        if cur and index == 0:  # check if we found wt we needed
            node, next, prev = Node(val), cur, cur.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev


    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next  # this lets me start at the real head of the linked list
        while cur and index > 0:  # transverse the list until we get to index
            cur = cur.next
            index -= 1
        if cur and cur != self.tail and index == 0:  # check if we found wt we needed
            next,prev =cur.next, cur.prev
            next.prev = prev
            prev.next = next