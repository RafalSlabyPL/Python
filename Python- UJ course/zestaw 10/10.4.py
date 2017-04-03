import random as r

class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def is_full(self):
        return False

    def put(self, data): #kolejka w pythonie nigdy nie bedzie przepelniona, lub mozna sztucznie narzucic limit identycznie jak w zadaniu poprzednim
        self.items.append(data)

    def get(self):
        if len(self.items) == 0:
            raise Exception("Queue is empty")
        else:
            return self.items.pop(0)

a = Queue()
print a.is_empty()
print "Zawartosc kolejki: ", a
print "Dodaje 10 losowych wartosci"
for number in range(10):
    a.put(r.randrange(0, 20))
print "Zawartosc kolejki: ", a
print a.get()
print "Zawartosc kolejki: ", a
