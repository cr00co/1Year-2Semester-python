class NodeList():
    def __init__(self, data):
        self.data = data
        self.next = None

# FIFO
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, data):
        node = NodeList(data)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node

    def get(self):
        if not self.head:
            raise IndexError("queue is empty")
        value = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value

    def is_empty(self):
        return self.head is None

#LIFO
class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = NodeList(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if not self.head:
            raise IndexError("stack is empty")
        value = self.head.data
        self.head = self.head.next
        return value
    
    def peek(self):
        if not self.head:
            raise IndexError("stack is empty")
        value = self.head.data
        return value

    def is_empty(self):
        return self.head is None

# Double-ended queue
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        node = NodeList(data)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node

    def push_back(self, data):
        node = NodeList(data)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node

    def pop_front(self):
        if not self.head:
            raise IndexError("deque is empty")
        value = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return value

    def pop_back(self):
        if not self.tail:
            raise IndexError("deque is empty")
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return value

    def is_empty(self):
        return self.head is None 

print("FIFO:")

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.get()

node = q.head
while node:
    print(node.data)
    node = node.next


print("------------")

print("LIFO:")

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
s.peek()

node = s.head
while node:
    print(node.data)
    node = node.next

print(s.peek())

print("------------")

print("Deque:")
d = Deque()
d.push_back(2)
d.push_back(3)
d.push_front(1)
d.push_back(4)
d.pop_front()
d.pop_back()

node = d.head
while node:
    print(node.data)
    node = node.next
