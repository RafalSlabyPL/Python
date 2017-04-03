import rectangle
import unittest


class FracModuleTest(unittest.TestCase):
    def setUp(self):
        self.RectangleA = rectangle.Rectangle(-1, -1, 1, 1)
        self.RectangleB = rectangle.Rectangle(0, 0, 2, 2)

    def test_str_rectangle(self):
        self.assertEquals(str(self.RectangleA), "['[-1, -1]', '[1, 1]', '[1, -1]', '[-1, 1]']")
        self.assertEquals(str(self.RectangleB), "['[0, 0]', '[2, 2]', '[2, 0]', '[0, 2]']")

    def test_repr_rectangle(self):
        self.assertEquals(self.RectangleA.__repr__(), 'Rectangle(-1, -1, 1, 1)')
        self.assertEquals(self.RectangleB.__repr__(), 'Rectangle(0, 0, 2, 2)')

    def test_eq_rectangle(self):
        self.assertTrue(self.RectangleA == rectangle.Rectangle(-1, -1, 1, 1))
        self.assertTrue(self.RectangleB == rectangle.Rectangle(0, 0, 2, 2))

    def test_ne_rectangle(self):
        self.assertTrue(self.RectangleA != rectangle.Rectangle(-2, -2, 2, 2))

    def test_center_rectangle(self):
        self.assertEquals(self.RectangleA.center(), [0, 0])
        self.assertEquals(self.RectangleB.center(), [1, 1])

    def test_area_rectangle(self):
        self.assertEquals(self.RectangleA.area, 4.0)
        self.assertEquals(self.RectangleB.area, 4.0)

    def test_move_rectangle(self):
        self.RectangleA.move(1,1)
        self.assertTrue(str(self.RectangleA) == str(self.RectangleB))

    def test_intersection_rectangle(self):
        self.assertEquals(str(self.RectangleA.intersection(self.RectangleB)), "['[0, 0]', '[1, 1]', '[1, 0]', '[0, 1]']")

    def test_cover_rectangle(self):
        self.assertEquals(str(self.RectangleA.cover(self.RectangleB)), "['[-1, -1]', '[2, 2]', '[2, -1]', '[-1, 2]']")

    def test_make4_rectangle(self):
        self.assertEquals(str(self.RectangleA.make4()), "[Rectangle(-1, -1, 0, 0), Rectangle(1, 1, 0, 0), Rectangle(1, -1, 0, 0), Rectangle(-1, 1, 0, 0)]")
        self.assertEquals(str(self.RectangleB.make4()), "[Rectangle(0, 0, 1, 1), Rectangle(2, 2, 1, 1), Rectangle(2, 0, 1, 1), Rectangle(0, 2, 1, 1)]")

    def tearDown(self):
        self.RectangleA.kill()
        self.RectangleB.kill()

if __name__ == '__main__':
    unittest.main()