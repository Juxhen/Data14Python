import random as r
from hangmanWords import word_list


class Logic:

    def __init__(self):
        self.__word = r.choice(word_list)
        self.length = len(self.__word)

    def get_word(self):
        return self.__word.upper()

    def get_new_word(self):
        self.__word = r.choice(word_list)
        return self.__word


winning_word = Logic()

