import circle
import unittest


class FracModuleTest(unittest.TestCase):
    def setUp(self):
        self.CircleA = circle.Circle(-1, -1, 1)
        self.CircleB = circle.Circle(0, 0, 2)

    def test_repr(self):
        self.assertEquals(self.CircleA.__repr__(), "Circle(-1, -1, 1)")
        self.assertEquals(self.CircleB.__repr__(), "Circle(0, 0, 2)")

    def test_eq(self):
        self.assertFalse(self.CircleA == self.CircleB)
        self.assertTrue(self.CircleA == self.CircleA)

    def test__ne(self):
        self.assertTrue(self.CircleA != self.CircleB)
        self.assertFalse(self.CircleA != self.CircleA)

    def test_str(self):
        self.assertEquals(str(self.CircleA), "Circle [-1, -1] r = 1")
        self.assertEquals(str(self.CircleB), "Circle [0, 0] r = 2")

    def test_area(self):
        self.assertAlmostEqual(self.CircleA.area(), 3.14159265359)
        self.assertAlmostEquals(self.CircleB.area(), 12.5663706144)


    def test_move(self):
        self.assertNotEquals(str(self.CircleA), "Circle [0, 0] r = 1")
        self.CircleA.move(1, 1)
        self.assertEquals(str(self.CircleA), "Circle [0, 0] r = 1")
        self.CircleA.move(-1, -1) # przywracam poczatkowa pozycje

    def test_cover(self):
        self.assertAlmostEquals(str(self.CircleA.cover(circle.Circle(1, 1, 1))), "Circle [0.0, 0.0] r = 4.82842712475")
        self.assertRaises(TypeError, self.CircleA.cover, "Blad")

    def tearDown(self):
        self.CircleA.kill()
        self.CircleB.kill()