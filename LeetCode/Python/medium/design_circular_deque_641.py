"""
641. Design Circular Deque
https://leetcode.com/problems/design-circular-deque/
"""


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.curr_size = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value, None, self.head)
        if self.getFront() != -1:
            self.head.prev = new_node
        self.head = new_node
        if self.getRear() == -1:
            self.tail = self.head
        self.curr_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value, self.tail, None)
        if self.getRear() != -1:
            self.tail.next = new_node
        self.tail = new_node
        if self.getFront() == -1:
            self.head = self.tail
        self.curr_size += 1
        return True

    def deleteFront(self) -> bool:
        if self.getFront() != -1:
            self.head = self.head.next
            self.curr_size -= 1
            if self.isEmpty():
                self.head = None
                self.tail = None
            return True
        return False

    def deleteLast(self) -> bool:
        if self.getRear() != -1:
            self.tail = self.tail.prev
            self.curr_size -= 1
            if self.isEmpty():
                self.head = None
                self.tail = None
            else:
                self.tail.next = None
            return True
        return False

    def getFront(self) -> int:
        return self.head.val if self.head else -1

    def getRear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return self.curr_size == 0

    def isFull(self) -> bool:
        return self.size == self.curr_size

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
