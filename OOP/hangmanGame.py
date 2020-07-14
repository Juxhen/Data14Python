from hangmanWords import word_list
import hangmanLogic as hl
import random as r
import time as t

#

class Game:

    def __init__(self):
        self.secret_list = []
        self.user_guess_list = []
        self.lives = 100
        self.winning_word = hl.winning_word.get_word()
        self.name = ""
        self.level_choice = ""
        self.new_health = None
        self.display_list_str = None

    def get_welcome(self):
        print("\n")
        print("Welcome to Juxhen's Random Number Generator Hangman\n")

    def get_user(self):
        self.name = input("Please enter your name\n").upper()
        if self.name.isalpha():
            print(f"Welcome {self.name} I wish you the best of luck lets start!")
            return True
        else:
            print("Please enter letters only!")
            return False

    def get_levels(self):
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

    def get_health(self, lives_in_health, damage_taken): # previous arguments (self,lives_in_health,damange_taken)
        if lives_in_health - damage_taken < 0:
            self.new_health = 0
            print(f"Congratulations, you're dead, the word was: {hl.winning_word}")
        else:
            self.new_health = lives_in_health - damage_taken
            t.sleep(1)
            print(f"sorry you lost {self.damage_taken} HP you are at {self.new_health} HP")
        return self.new_health

    def add_to_list(self):
        for letter in hl.winning_word:
            self.secret_list.append(letter)

    def add_blanks(self):
        self.display_list = []
        for blanks in range(0, len(self.secret_list)):
            self.display_list.append("_")
            self.display_list_str = " ".join(self.display_list)
        return self.display_list_str

    def functionality(self):
        word_completed = False
        while not word_completed and lives > 0:
            user_guess = input("Guess a letter!\n").upper()
            if user_guess.isalpha() and len(user_guess) == 1:
                if user_guess in self.user_guess_list:
                    print(f"sorry you have already guessed {user_guess} please pick another letter")
                elif user_guess not in self.secret_list:
                    health_loss_rng = r.randint(1, 10)
                    lives = self.get_health(lives, health_loss_rng)
                else:
                    self.user_guess_list.append(user_guess)
                    index_counter = 0
                    for letter in self.secret_list:
                        if letter == user_guess:
                            self.display_list[index_counter] = letter
                        index_counter += 1
                    t.sleep(1)
                    print(f"Horray you matched the letter {user_guess}")
                    if "_" not in self.display_list:
                        print(f"Congratulations, the word was: {hl.winning_word}")
                        word_completed = True
                    display_list_str = " ".join(self.display_list)
                    print(f"{display_list_str}")
            else:
                print(f"sorry {user_guess} is not a letter")