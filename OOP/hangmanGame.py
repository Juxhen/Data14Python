from hangmanWords import word_list
import hangmanLogic as hl
import random as r
import time as t

secret_list = []
user_guess_list = []
display_list = []
lives = 100
winning_word = hl.winning_word.get_word()

print("\n")
print("Welcome to Juxhen's Random Number Generator Hangman\n")


def user():
    name = input("Please enter your name\n").upper()
    if name.isalpha():
        print(f"Welcome {name} I wish you the best of luck lets start!")
        return True
    else:
        print("Please enter letters only!")
        return False


name_check = user()
while not name_check:
    user()


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

level_check = levels()

if level_check == 100:
    lives = 100
elif level_check == 70:
    lives = 70
elif level_check == 50:
    lives = 50


def health(lives_in_health, damage_taken):
    if lives_in_health - damage_taken < 0:
        new_health = 0
        print(f"Congratulations, you're dead, the word was: {winning_word}")
    else:
        new_health = lives_in_health - damage_taken
        print(f"sorry you lost {damage_taken} HP you are at {new_health} HP")
    return new_health


for letter in winning_word:
    secret_list.append(letter)
# print(secret_list)

for blanks in range(0, len(secret_list)):
    display_list.append("_")
    display_list_str = " ".join(display_list)
print(display_list_str)

word_completed = False

while not word_completed and lives > 0:
    user_guess = input("Guess a letter!\n").upper()
    if user_guess.isalpha() and len(user_guess) == 1:
        if user_guess in user_guess_list:
            print(f"sorry you have already guessed {user_guess} please pick another letter")
        elif user_guess not in secret_list:
            health_loss_rng = r.randint(1,10)
            lives = health(lives, health_loss_rng)
        else:
            user_guess_list.append(user_guess)
            index_counter = 0
            for letter in secret_list:
                if letter == user_guess:
                    display_list[index_counter] = letter
                index_counter += 1
            print(f"Horray you matched the letter {user_guess}")
            if "_" not in display_list:
                print(f"Congratulations, the word was: {winning_word}")
                word_completed = True
            display_list_str = " ".join(display_list)
            print(f"{display_list_str}")
    else:
        print(f"sorry {user_guess} is not a letter")
