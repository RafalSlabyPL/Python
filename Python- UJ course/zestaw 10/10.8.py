import random as r

class RandomQueue:

    def __init__(self):
        self.list =[]
        pass
    def __str__(self):
        return str(self.list)

    def insert(self, item):
        self.list.append(item)
        pass

    def remove(self):   # zwraca losowy element
        return self.list.pop(r.randrange(0, len(self.list)))

    def is_empty(self):
        if len(self.list)==0:
            return True
        else:
            return False

    def is_full(self):   #nigdy nie jest oelna
        return False

a = RandomQueue()
print "Czy kolejka jest pusta: ", a.is_empty()
print "Dodaje losowy element do kolejki"
a.insert (r.randrange(0,20))
print "Zawartosc kolejki: ", a
print "remove: ", a.remove()
print "Dodaje wartosci od 1 do 20"
for x in range(1,21):
    a.insert(x)
print "zawartos kolejki: ", a
"Wypisuje wszystkie 20 wartosci"
for x in range(1,21):
    print "%s:  " % x, a.remove()