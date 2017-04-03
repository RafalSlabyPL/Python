from math import sqrt
pi = 3.14159265359

class Circle:
    """Klasa reprezentujaca okregi na plaszczyznie."""

    def __init__(self, x=0, y=0, radius=1):
        if radius <= 0 or not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Wrong input")
        self.pt = [x, y]
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        return 'Circle(%s, %s, %s)' % (self.pt[0], self.pt[1], self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "Circle [%s, %s] r = %s" %(self.pt[0], self.pt[1], self.radius)

    def area(self):           # pole powierzchni
        return pi * self.radius * self.radius

    def move(self, x, y):     # przesuniecie o (x, y)
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError
        else:
            self.pt[0] += x
            self.pt[1] += y
        pass

    def cover(self, other):
        if not isinstance(other, Circle):
            raise TypeError
        else:
            new_radius = sqrt((self.pt[0]-other.pt[0])**2 + (self.pt[1]-other.pt[1])**2) + self.radius + other.radius
            new_x = (self.pt[0] + other.pt[0]) / 2.0
            new_y = (self.pt[1] + other.pt[1]) / 2.0
            return Circle(new_x, new_y, new_radius)

    def kill(self):
        del self
        pass