import unittest
import fracs as f

class FracModuleTest(unittest.TestCase):
    def setUp(self):
        self.f1 = f.frac(-1, 2)  # -1/2
        self.f2 = f.frac(0, 2)   # zero
        self.f3 = f.frac(3, 1)   # 3
        self.f4 = f.frac(6, 2)   # 3 (niejednoznacznosc)
        self.f5 = f.frac(0, 2)   # zero (niejednoznacznosc)
        self.f6 = f.frac(6, 1)   # 6

    def test_add_frac(self):
        self.assertEquals(self.f4 + self.f3 + self.f2, self.f6)

    def test_sub_frac(self):
        self.assertEquals(self.f6 - self.f4, self.f3)

    def test_mul_frac(self):
        self.assertEquals(self.f6 - self.f4, self.f3)

    def test_div_frac(self):
        self.assertEquals(self.f4 / self.f1, f.frac(-6, 1))

    def test_is_positive(self):
        self.assertEquals(self.f1.is_positive(), False)
        self.assertEquals(self.f4.is_positive(), True)

    def test_is_zero(self):
        self.assertEquals(self.f4.is_zero(), False)
        self.assertEquals(self.f2.is_zero(), True)

    def test_cmp_frac(self):
        self.assertTrue(self.f6 > self.f4)
        self.assertTrue(self.f1 < self.f4)
        self.assertTrue(self.f3 == self.f4)
        self.assertTrue(self.f3 <= self.f4)

    def test_frac2float(self):
        self.assertTrue(float(self.f6) == 6)
        self.assertTrue(float(self.f1) == -0.5)

    def test_neg_frac(self):
        self.assertEquals(-self.f1, f.frac(1, 2))

    def __pos__(self):
        self.assertEquals(+self.f1, f.frac(-1, 2))

    def test_invert_frac(self):
        self.assertEquals(float(self.f1.__invert__()), -2)

    def tearDown(self):
        self.f1.kill()
        self.f2.kill()
        self.f3.kill()
        self.f4.kill()
        self.f5.kill()
        self.f6.kill()


if __name__ == '__main__':
    unittest.main()
