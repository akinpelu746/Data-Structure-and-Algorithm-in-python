class quack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.stack3 = []
        self.length = 0

    def push(self, x):
        self.length += 1
        self.stack1.append(x)
        return self.stack1

    def pop(self):
        try:
            if self.length > 0:
                self.length -= 1
            return self.stack1.pop()
        except:
            raise IndexError("Stack is empty")

    def pull(self):
        try:
            if self.length > 0:
                for i in range(self.length):
                    self.stack2.append(self.stack1.pop())
                self.stack3.append(self.stack2.pop())
                self.length -= 1
                for i in range(self.length):
                    self.stack1.append(self.stack2.pop())

            return self.stack3.pop()
        except:
            raise IndexError("Stack is empty")


