import rekurencja
import unittest

class FactorialAndFibonacciTest(unittest.TestCase):
    def test_Factorial(self):
        self.assertEquals(rekurencja.factorial(7), 5040)

    def test_Fibonacci(self):
        self.assertEquals(rekurencja.fibonacci(8), 21)

if __name__ == '__main__':
    unittest.main()
