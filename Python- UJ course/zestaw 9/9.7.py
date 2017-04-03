from random import randint


class Node(object):
    def __init__(self, poziom):
        self.poziom = poziom
        self.value = randint(0, 20)
        self.left = None
        self.right = None
        if (randint(1, 2)) % 2 == 0:
            self.left = Node(self.poziom + 1)
            self.right = Node(self.poziom + 1)
            print("Poziom wezla: ", self.poziom, "Przechwywania wartosc liczbowa: ", self.value)
        else:
            print("Poziom wezla: ", self.poziom, "Przechwywania wartosc liczbowa: ", self.value, "- to jest lisc")

    def count_top(self):
        if self.left == None and self.right == None:
            return int(self.value)
        else:
            return int(self.left.count_top() + self.right.count_top() + self.value)

    def count_leafs (self):
        if self.left == None and self.right == None:
            return 1
        else:
            return int(self.left.count_leafs() + self.right.count_leafs())


class Tree(object):
    def __init__(self):
        self.name = "root"
        print("TWORZE NOWE DRZEWO")
        print("Generowanie wezlow:")
        self.left = Node(1)
        self.right = Node(1)
        self.value = randint(0, 20)
        self.poziom =0
        print("Poziom wezla: ", self.poziom, "Przechwywania wartosc liczbowa: ", self.value)

    def count_top(self):
        return self.value + self.left.count_top() + self.right.count_top()

    def count_leafs(self):
        return self.left.count_leafs() + self.right.count_leafs()


drzewo = Tree()
print("Suma lisci w drzewie: ", drzewo.count_leafs())
print("Suma wartosci przechowywanych w drzewie: ", drzewo.count_top())

