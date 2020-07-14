from hangmanWords import word_list
import hangman_brain as hl
import random as r
import time as t

secret_list = []
user_guess_list = []
display_list = []
lives = 100
winning_word = hl.winning_word.get_word()

def welcome_message():
    print("\n")
    print("Welcome to Juxhen's Random Number Generator Hangman\n")


def user():
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


def levels():
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

# hp = levels()

def string_to_list(string = ""):
    new_list = []
    for letter in string:
        new_list.append(letter)
    return new_list

def create_display_list(length):
    new_list = []
    for blanks in range(0, length):
        new_list.append("_")
    return new_list

# create_display_list(len(secret_list))

# takes guess from user
def get_guess():
    user_guess = input("Guess a letter!\n")
    return user_guess

# prevents user from continuing if guess is not alphabetical
def valid_guess(guess):
    guess_is_valid = False
    while not guess_is_valid:
        if guess.isalpha() and len(guess) == 1:
            guess_is_valid = True
            return guess.upper()
        else:
            print("That's not a letter")
            guess_is_valid = False
            guess = get_guess()

def ensure_new_letter(guess, guess_list = []):
    guess_is_new = False
    while not guess_is_new:
        if guess in guess_list:
            print(f"sorry you have already guessed {guess} please pick another letter")
            guess = get_guess()
            valid_guess(guess)
            guess_is_new = False
        else:
            guess_list.append(guess)
            guess_is_new = True
    return [guess, guess_list]


def final_guess():
    return ensure_new_letter(valid_guess(get_guess()))


def not_in_list(guess, list_with_correct_word):
    if guess not in list_with_correct_word:
        health_loss = r.randint(1, 10)
    else:
        health_loss = 0
    return health_loss


def health(lives_in_health, guess, list_with_correct_word):
    damage_taken = not_in_list(guess, list_with_correct_word)
    if lives_in_health - damage_taken < 0:
        new_health = 0
        print(f"Congratulations, you're dead, the word was: {winning_word}")
        # new_game()
        return new_health
    elif damage_taken == 0:
        return lives_in_health
    else:
        new_health = lives_in_health - damage_taken
        print(f"sorry you lost {damage_taken} HP you are at {new_health} HP")
    return new_health


def look_for_letter(guess, hidden_word, displayed_list):
    index_counter = 0
    letter_in_word = False
    for letter in hidden_word:
        if letter == guess:
            displayed_list[index_counter] = letter
            letter_in_word = True
        index_counter += 1
    if letter_in_word:
        print(f"Hooray, you matched the letter {letter}")
    if "_" not in display_list:
        print(f"Congratulations, the word was: {hidden_word}")
        # new_game()
    return displayed_list



# welcome_message()
# user()
# hp = levels()
# print(create_display_list(6))
# final_guess()
# not_in_list()
# health()
# look_for_letter()











# def new_game():
    #""" Insert option to play again """


# display_list_str = " ".join(display_list)
# print(f"{display_list_str}")

#  guess = valid_guess()[0]
#  list_of_guesses = valid_guess[1]

# word_completed = False
# while not word_completed and lives > 0:
#     user_guess = input("Guess a letter!\n").upper()
#     if user_guess.isalpha() and len(user_guess) == 1:
#         if user_guess in user_guess_list:
#             print(f"sorry you have already guessed {user_guess} please pick another letter")
#         elif user_guess not in secret_list:
#             health_loss_rng = r.randint(1,10)
#             lives = health(lives, health_loss_rng)
        # else:
        #     user_guess_list.append(user_guess)
        #     index_counter = 0
        #     for letter in secret_list:
        #         if letter == user_guess:
        #             display_list[index_counter] = letter
        #         index_counter += 1
        #     t.sleep(1)
        #     print(f"Horray you matched the letter {user_guess}")
    #         if "_" not in display_list:
    #             print(f"Congratulations, the word was: {winning_word}")
    #             winning_word = hl.winning_word.get_new_word()
    #             word_completed = True
    #         display_list_str = " ".join(display_list)
    #         print(f"{display_list_str}")
    # else:
    #     print(f"sorry {user_guess} is not a letter")


# to replay with a different word
# winning_word = hl.winning_word.get_new_word()