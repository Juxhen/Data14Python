from scrabble_game import ScrabbleCalc

    def test_score_calculator():
        assert ScrabbleCalc.add_to_score("a") == 1
        assert ScrabbleCalc.add_to_score("g") == 2
        assert ScrabbleCalc.add_to_score("b") == 3
        assert ScrabbleCalc.add_to_score("v") == 4
        assert ScrabbleCalc.add_to_score("k") == 5
        assert ScrabbleCalc.add_to_score("x") == 8
        assert ScrabbleCalc.add_to_score("z") == 10


    def test_correct_length():
        assert len(ScrabbleCalc.starting_letters()) == 7


