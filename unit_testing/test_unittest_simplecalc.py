from simple_calc import SimpleCalc
import unittest

class Calctests(unittest.TestCase):
    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(1, 1), 2)
        self.assertEqual(self.calc.add(-5, -2), -7)
        self.assertEqual(self.calc.add(0, 10), 10)
        self.assertIsNotNone(self.calc.add(0, 0))

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.subtract(1, 6), -5)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        self.assertIsNotNone(self.calc.subtract(0, 0))

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(1, 1), 1)
        self.assertEqual(self.calc.multiply(-5, -2), 10)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertIsNotNone(self.calc.multiply(0, 0))

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(1, 4), 0.25)
        self.assertEqual(self.calc.divide(-5, -2), 2.5)
        self.assertEqual(self.calc.divide(0, 10), 0)
