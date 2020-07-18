from scrabble_game import ScrabbleCalc
import unittest


class ScrabbleTests(unittest.TestCase):

    def test_score_calculator(self):
        self.assertEqual(my_scrabble.score_calculator("a") == 1)
        self.assertEqual(my_scrabble.score_calculator("g") == 2)
        self.assertEqual(my_scrabble.score_calculator("b") == 3)
        self.assertEqual(my_scrabble.score_calculator("v") == 4)
        self.assertEqual(my_scrabble.score_calculator("k") == 5)
        self.assertEqual(my_scrabble.score_calculator("x") == 8)
        self.assertEqual(my_scrabble.score_calculator("z") == 10)


my_scrabble = ScrabbleTests()
