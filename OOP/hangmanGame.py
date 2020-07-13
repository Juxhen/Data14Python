from hangmanWords import word_list
import hangmanLogic as hl
import random as r
import time as t

secret_list = []
user_guess_list = []
display_list = []
lives = 70

def health(lives, damage_taken):
    if lives - damage_taken < 0:
        newHealth = 0
        print("gg you're dead! - Try again")
    else:
        newHealth = lives - damage_taken
        print(f"sorry you lost {damage_taken} HP you are at {newHealth} HP")
    return newHealth

winning_word = hl.winning_word.get_word()

for letter in winning_word:
    secret_list.append(letter)
# print(secret_list)

for blanks in range(0, len(secret_list)):
    display_list.append("_")
print(display_list)

word_completed = False

while not word_completed and lives > 0:
    user_guess = input("Guess a letter!\n").upper()
    if user_guess.isalpha() and len(user_guess) == 1:
        if user_guess in user_guess_list:
            print(f"sorry you have already guessed {user_guess} please pick another letter")
        elif user_guess not in secret_list:
            healthlossrng = r.randint(5,10)
            lives = health(lives, healthlossrng)
        else:
            user_guess_list.append(user_guess)
            index_counter = 0
            for letter in secret_list:
                if letter == user_guess:
                    display_list[index_counter] = letter
                index_counter += 1
            print(f"Horray you matched the letter {user_guess}")
            print(f"{display_list}")

    else:
        print(f"sorry {user_guess} is not a letter")