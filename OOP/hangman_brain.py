import random as r
from hangmanWords import word_list


class Logic:

    def __init__(self):
        self.__word = r.choice(word_list)
        self.length = len(self.__word)

    def get_word(self):
        return self.__word.upper()

    def get_new_word(self):
        new_word = r.choice(word_list)
        if self.word == winning_word:
            new_word = r.choice(word_list)
        return new_word


winning_word = Logic()

