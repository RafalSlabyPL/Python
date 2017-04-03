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
        return [(self.pt1[0]+self.pt2[0])/2,(self.pt1[1]+self.pt2[1])/2]

    def area(self):             # pole powierzchni
        x = math.fabs(self.pt1[0] - self.pt2[0])
        y = math.fabs(self.pt1[1] - self.pt2[1])
        return x*y

    def move(self, x, y):       # przesuniecie o (x, y)
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
            raise Exception(TypeError)
        self.pt1[0] += x
        self.pt1[1] += y
        self.pt2[0] += x
        self.pt2[1] += y
        self.pt3 = [self.pt2[0], self.pt1[1]] #prawy dolny rog
        self.pt4 = [self.pt1[0], self.pt2[1]] #lewy gorny rog
        pass

    def intersection(self, other):
        if not isinstance(other, Rectangle):
            raise Exception(TypeError)
        else:
            other.min_x = min (other.pt1[0], other.pt2[0])
            other.max_x = max (other.pt1[0], other.pt2[0])
            other.min_y = min (other.pt1[1], other.pt2[1])
            other.max_y = max (other.pt1[1], other.pt2[1])
            self.min_x = min (self.pt1[0], self.pt2[0])
            self.max_x = max (self.pt1[0], self.pt2[0])
            self.min_y = min (self.pt1[1], self.pt2[1])
            self.max_y = max (self.pt1[1], self.pt2[1])
            x1 = max(self.min_x, other.min_x)
            y1 = max(self.min_y, other.min_y)
            x2 = min (self.max_x, other.max_x)
            y2 = min (self.max_y, other.max_y)
            return Rectangle(x1, y1, x2, y2)

    def make4(self):
        if self.pt1[0] == self.pt2[0] or self.pt1[1] == self.pt2[1]:
            raise Exception("Thats not rectangle")
        else:
            center = self.center()
            a = Rectangle(self.pt1[0], self.pt1[1], center[0], center[1])
            b = Rectangle(self.pt2[0], self.pt2[1], center[0], center[1])
            c = Rectangle(self.pt3[0], self.pt3[1], center[0], center[1])
            d = Rectangle(self.pt4[0], self.pt4[1], center[0], center[1])
            return [a, b, c, d]

    def cover(self, other):
        if not isinstance(other, Rectangle):
            raise Exception(TypeError)
        else:
            min_x = min(self.pt1[0], self.pt2[0], other.pt1[0], other.pt2[0])
            max_x = max(self.pt1[0], self.pt2[0], other.pt1[0], other.pt2[0])
            min_y = min(self.pt1[1], self.pt2[1], other.pt1[1], other.pt2[1])
            max_y = max(self.pt1[1], self.pt2[1], other.pt1[1], other.pt2[1])
            return Rectangle(min_x, min_y, max_x, max_y)

    def kill(self):
        del self

#RectangleA = Rectangle(-1, -1, 1, 1)
#RectangleB = Rectangle(0, 0, 2, 2)
