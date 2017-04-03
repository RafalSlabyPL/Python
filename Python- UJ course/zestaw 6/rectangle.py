import math


class Rectangle:
    """Klasa reprezentujaca prostokat na plaszczyznie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.pt1 = [x1, y1] #lewy dolny rog
        self.pt2 = [x2, y2] #prawy gorny rog
        self.pt3 = [x2, y1] #prawy dolny rog
        self.pt4 = [x1, y2] #lewy gorny rog
        self.area = self.area()
        pass

    def __str__(self):               # "[(x1, y1), (x2, y2)]"
        return str([str(self.pt1), str(self.pt2), str(self.pt3), str(self.pt4)])

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return 'Rectangle(%s, %s, %s, %s)' % (self.pt1[0], self.pt1[1], self.pt2[0], self.pt2[1])

    def __eq__(self, other):        # obsluga rect1 == rect2

        return self.area == other.area

    def __ne__(self, other):        # obsluga rect1 != rect2
        return not self.area == other.area

    def center(self):          # zwraca srodek prostokata
        return [(self.pt1[0] + self.pt2[0]) / 2, (self.pt1[1] + self.pt2[1]) / 2]

    def area(self):             # pole powierzchni
        x=math.fabs(self.pt1[0]-self.pt2[0])
        y=math.fabs(self.pt1[1]-self.pt2[1])
        return x*y

    def move(self, x, y):       # przesuniecie o (x, y)
        self.pt1[0] += x
        self.pt1[1] += y
        self.pt2[0] += x
        self.pt2[1] += y
        self.pt3 = [self.pt2[0], self.pt1[1]] #prawy dolny rog
        self.pt4 = [self.pt1[0], self.pt2[1]] #lewy gorny rog
        pass

    def kill(self):
        del self

RectangleA = Rectangle(-1, -1, 1, 1)
print str(RectangleA.move(1, 1))