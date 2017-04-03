class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):
        if len(self.items) == 10:
            return True
        else:
            return False

    def push(self, item):
        if len (self.items) ==10:
            raise Exception("Stack is full")
        else:
            self.items.append(item)
            pass

    def pop(self):
        if len(self.items) == 0:
            raise Exception("Stack is empty")
        else:
            return self.items.pop()



stos = Stack()
print "Czy stos pusty: ", stos.is_empty()
for x in range (1, 11, 1):
    stos.push(x)
print(stos)
print "pop: ", (stos.pop())
print(stos)
print "push 20"
stos.push(20)
print "Czy stos pelny: ", (stos.is_full())