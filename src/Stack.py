class Stack():
    """Implementation of stack data structure"""

    def __init__(self):
        """Initiate stack list and length"""
        self.stack = []
        self.length = 0

    def pop(self):
        """pop the last element in the stack"""
        if self.length == 0:
            return "stack is empty"

        self.length -= 1
        return self.stack.pop()

    def push(self, data):

        self.stack.append(data)
        self.length += 1

    def peek(self):
        if self.length == 0:
            return "stack is empty"
        return self.stack[self.length - 1]


stack = Stack()
assert stack.pop() == "stack is empty"
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.peek()
