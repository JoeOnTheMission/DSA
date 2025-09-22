class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class MyStack:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def push(self, val: int) -> None:
        last = self.tail.prev
        node = Node(val)
        # edit 4 pointers
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def pop(self) -> int:
        ans =  self.tail.prev
        before =  self.tail.prev.prev
        # edit 2 pointers
        self.tail.prev = before
        before.next = self.tail
        return ans.value

    def top(self) -> int:
        ans =  self.tail.prev
        return ans.value

    def empty(self) -> bool:
        if self.head.next ==  self.tail:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()