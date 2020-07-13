import random as r
from hangmanWords import word_list


class Logic:

    def __init__(self):
        self.word = r.choice(word_list)

    def get_word(self):
        return self.word.upper()

    def word_length(self):
        return len(self.word)


winning_word = Logic()


