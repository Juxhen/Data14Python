from scrabble_game import ScrabbleCalc
import unittest

class ScrabbleTests(unittest.TestCase):
    my_scrabble = ScrabbleCalc()

    def test_score_calculator(self):
        self.letters = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
                        'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
                        'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
                        's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
                        'y': 4, 'z': 10}
        self.start_score = 0
        #self.letters.keys()
        for x in self.letters:
            print(x, self.letters[x])
            if self.letters[x] == 1:
                self.start_score += 1
            elif
    #     # self.assertEqual(self.calc.add(2, 2), 4)
    #     # self.assertEqual(self.calc.add(1, 1), 2)
    #     # self.assertEqual(self.calc.add(-5, -2), -7)
    #     # self.assertEqual(self.calc.add(0, 10), 10)
    #     # self.assertIsNotNone(self.calc.add(0, 0))
    #
    # def test_subtract(self):
    #     self.assertEqual(self.calc.subtract(2, 2), 0)
    #     self.assertEqual(self.calc.subtract(1, 6), -5)
    #     self.assertEqual(self.calc.subtract(-5, -2), -3)
    #     self.assertEqual(self.calc.subtract(0, 10), -10)
    #     self.assertIsNotNone(self.calc.subtract(0, 0))
    #
    # def test_multiply(self):
    #     self.assertEqual(self.calc.multiply(2, 2), 4)
    #     self.assertEqual(self.calc.multiply(1, 1), 1)
    #     self.assertEqual(self.calc.multiply(-5, -2), 10)
    #     self.assertEqual(self.calc.multiply(0, 10), 0)
    #     self.assertIsNotNone(self.calc.multiply(0, 0))
    #
    # def test_divide(self):
    #     self.assertEqual(self.calc.divide(2, 2), 1)
    #     self.assertEqual(self.calc.divide(1, 4), 0.25)
    #     self.assertEqual(self.calc.divide(-5, -2), 2.5)
    #     self.assertEqual(self.calc.divide(0, 10), 0)

my_scrab = ScrabbleTests()
my_scrab.test_score_calculator()