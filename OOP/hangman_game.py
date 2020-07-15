import hangman_brain as hl
import random as r

winning_word = hl.winning_word.get_word()


class Game:

    def __init__(self):
        self.welcome_message()
        self.secret_list = []
        self.user_guess_list = []
        self.lives = 100
        self.display_list = []
        self.user()
        self.levels()
        self.get_guess()
        self.string_to_list(winning_word)
        self.create_display_list(len(self.string_to_list()))
        self.valid_guess(self.get_guess())
        self.look_for_letter(self.get_guess(), winning_word, self.display_list)

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

    def string_to_list(self, string=winning_word):
        new_list = []
        for letter in string:
            new_list.append(letter)
        return new_list

    def create_display_list(self, length):
        new_list = []
        for blanks in range(0, length):
            new_list.append("_")
        return new_list

    def get_guess(self):
        user_guess = input("Guess a letter!\n")
        self.valid_guess()
        return user_guess

    # prevents user from continuing if guess is not alphabetical
    def valid_guess(self, user_guess):
        guess_is_valid = False
        while not guess_is_valid:
            if user_guess.isalpha() and len(user_guess) == 1:
                self.ensure_new_letter(user_guess)
                return user_guess.upper()
            else:
                print("That's not a letter")
                guess_is_valid = False
                user_guess = self.get_guess()

    def ensure_new_letter(self, guess, guess_list):
        if guess_list is None:
            guess_list = []
        guess_is_new = False
        while not guess_is_new:
            if guess in guess_list:
                print(f"sorry you have already guessed {guess} please pick another letter")
                guess = self.get_guess()
                self.valid_guess(guess)
                guess_is_new = False
            else:
                guess_list.append(guess)
                guess_is_new = True
        return [guess, guess_list]

    def final_guess(self):
        return self.ensure_new_letter(self.valid_guess(self.get_guess()))

    def not_in_list(self, guess, list_with_correct_word):
        if guess not in list_with_correct_word:
            health_loss = r.randint(1, 10)
        else:
            health_loss = 0
        return health_loss

    def health(self, lives_in_health, guess, list_with_correct_word):
        damage_taken = self.not_in_list(guess, list_with_correct_word)
        if lives_in_health - damage_taken < 0:
            new_health = 0
            print(f"Congratulations, you're dead, the word was: {winning_word}")
            # new_game = hl.winning_word.get_new_word()
            return new_health
        elif damage_taken == 0:
            return lives_in_health
        else:
            new_health = lives_in_health - damage_taken
            print(f"sorry you lost {damage_taken} HP you are at {new_health} HP")
        return new_health

    def look_for_letter(self, guess, hidden_word, displayed_list):
        global letter
        index_counter = 0
        letter_in_word = False
        for letter in hidden_word:
            if letter == guess:
                displayed_list[index_counter] = letter
                letter_in_word = True
            index_counter += 1
        if not letter_in_word:
            print(f"Hooray, you matched the letter {letter}")
            return displayed_list
        if "_" not in self.display_list:
            print(f"Congratulations, the word was: {hidden_word}")
            # new_game = hl.winning_word.get_new_word()
        return displayed_list


my_game = Game() # Object of Game class
