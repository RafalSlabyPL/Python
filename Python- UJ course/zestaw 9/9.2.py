class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def empty(self):
        if self.value == None:
            return True
        else:
            return False

    def push(self, value = None):
        if self.value == None:
            self.value = value
        else:
            if self.next == None:
                self.next = Node(value)
            else:
                self.next.push(value)
        pass

    def printing(self):
        print(self.value)
        if self.next is not None:
            self.next.printing()
        pass

    def laczenie(self, x):
        if self.next is not None:
            self.next.laczenie(x)
        else:
            self.next = x
        pass

    #def delete_font(self):
     #   if self.next is not None:
      #      self = self.next
       # else:
        #    Exception("Nothing to delete")
         #pass

def merage(kolejka1, kolejka2):
    if not isinstance(kolejka1, Node) or not isinstance(kolejka2, Node):
        raise Exception (TypeError)
    elif kolejka2.value == None:
        pass
    else:
        kolejka1.laczenie(kolejka2)
    return kolejka1




a = Node ()
print (a.empty())
a.push(1)
print(a.empty())
print("Drukowane listy z pojedyńczym elementem")
a.printing()
a.push(2)
a.push(3)
a.push(4)
print("Drukowanie listy z 4 elementami")
a.printing()
b = Node (5)
b.push(6)
b.push(7)
print("Drukowanie 2 polaczoonych")
c = merage(a, b)
c.printing()
print("Usuwanie")
del c
#c.printing()
