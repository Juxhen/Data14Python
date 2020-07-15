import hangman_brain as hb
import random as r


class Game:
    def __init__(self):
        self.user()
        self.word_guessed = False
        self.secret_word = hb.winning_word.get_word()
        self.attempts = len(self.secret_word) + 3
        self.secret_word_list = []
        self.user_guess_list = []
        self.user_guesses = []
        self.display_list = []
        self.display_list_str = ""
        #self.get_guessed_letter()
        self.run()
        self.continue_new_game = "Y"

    def user(self):
        correct_name = False
        while not correct_name:
            name = input("Please enter your name\n").capitalize()
            if name.isalpha():
                print(f"Hello {name}, let's play hangman!")
                correct_name = True
            else:
                print("Please enter letters")
                correct_name = False
        return name

    def list_view(self):
        for letter in self.secret_word:
            self.secret_word_list.append(letter)
            # print(secret_list)
        for blanks in range(0, len(self.secret_word_list)):
            self.display_list.append("_")
            self.display_list_str = " ".join(self.display_list)
        print(self.display_list_str)

    def run(self):
        while not self.word_guessed:
            user_guess = input("Guess a letter!\n").upper()
            if user_guess.isalpha() and len(user_guess) == 1:
                if user_guess in self.user_guess_list:
                    print(f"You have already guessed {user_guess}, please pick another letter")
                else:
                    self.user_guess_list.append(user_guess)
                    index_counter = 0
                    for letter in self.secret_word_list:
                        if letter == user_guess:
                            self.display_list[index_counter] = letter
                        index_counter += 1
                    print(f"Well done! {user_guess} is in the word")
                    if "_" not in self.display_list:
                        print(f"Congratulations, the word was: {self.secret_word}")
                        word_completed = True
                    self.display_list_str = " ".join(self.display_list)
                    print(f"{self.display_list_str}")
            else:
                print(f"sorry {user_guess} is not a letter")

    def continue_new_game(self):
        continue_game = input("Do you want to play again? Y to continue, any other key to quit\n")
        if continue_game.upper() == "Y":
            Game()
        else:
            print("Thank you for playing. See you next time!")

start_game = Game()