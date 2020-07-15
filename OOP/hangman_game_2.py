import sys

import hangman_brain as hl
import random as r


class Game:

    def __init__(self):
        self.welcome_message()
        self.user()
        self.word_completed = False
        self.word = hl.winning_word.get_word()
        self.secret_list = []
        self.user_guess_list = []
        self.display_list = []
        self.lives = self.levels()
        self.display_list_str = ""
        self.new_word = hl.winning_word.get_new_word()
        self.list_view()
        self.run()
        #self.new_game()
        #self.start_new_game()


    def welcome_message(self):
        print("\n")
        print("Welcome to Juxhen's Random Number Generator Hangman\n")

    def user(self):
        name_successful = False
        while not name_successful:
            name = input("Please enter your name\n").upper()
            if name.isalpha():
                print(f"Welcome {name} I wish you the best of luck lets start!")
                name_successful = True
            else:
                print("Please enter letters only!")
                name_successful = False
        return name

    def levels(self):
        level_choice = ""
        flag = False
        while not flag:
            level_choice = input("Please pick a level, 'Easy', 'Medium', 'Hard'\n").upper()
            if level_choice == "EASY":
                print("Easy it is!")
                return 100
                flag = True
            elif level_choice == "MEDIUM":
                print("Medium it is!")
                return 70
                flag = True
            elif level_choice == "HARD":
                print("Hard it is!")
                return 50
                flag = True
            else:
                print("Please enter a valid difficulty")
                flag = False

    def health(self, lives_in_health, damage_taken):
        if lives_in_health - damage_taken < 0:
            new_health = 0
            print(f"Congratulations, you're dead, the word was: {self.word}")
            self.new_game()
        else:
            new_health = lives_in_health - damage_taken
            print(f"sorry you lost {damage_taken} HP you are at {new_health} HP")
        return new_health

    def list_view(self):
        for letter in self.word:
            self.secret_list.append(letter)
            # print(secret_list)

        for blanks in range(0, len(self.secret_list)):
            self.display_list.append("_")
            self.display_list_str = " ".join(self.display_list)
        print(self.display_list_str)

    def run(self):
        while not self.word_completed and self.lives > 0:
            user_guess = input("Guess a letter!\n").upper()
            if user_guess.isalpha() and len(user_guess) == 1:
                if user_guess in self.user_guess_list:
                    print(f"sorry you have already guessed {user_guess} please pick another letter")
                elif user_guess not in self.secret_list:
                    health_loss_rng = r.randint(1, 10)
                    self.lives = self.health(self.lives, health_loss_rng)
                else:
                    self.user_guess_list.append(user_guess)
                    index_counter = 0
                    for letter in self.secret_list:
                        if letter == user_guess:
                            self.display_list[index_counter] = letter
                        index_counter += 1
                    print(f"Horray you matched the letter {user_guess}")
                    if "_" not in self.display_list:
                        print(f"Congratulations, the word was: {self.word}")
                        self.word_completed = True
                        self.new_game()
                    self.display_list_str = " ".join(self.display_list)
                    print(f"{self.display_list_str}")
            else:
                print(f"sorry {user_guess} is not a letter")


    def start_new_game(self):
        self.word = hl.winning_word.get_new_word()
        return self.word

    def new_game(self):
        choice = input("Would you like to play again? Yes/No\n").upper()
        if choice == "YES":
            self.start_new_game()
        else:
            print("Thank you for playing")
            sys.exit()

new_game = Game()