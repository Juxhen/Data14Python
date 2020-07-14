import random as r


def not_in_list(guess, list_with_correct_word):
    print(1)
    if guess not in list_with_correct_word:
        health_loss = r.randint(1, 10)
        print(health_loss)
    else:
        health_loss = 0
    print(3)
    return health_loss


def health(lives_in_health, guess, list_with_correct_word):
    damage_taken = not_in_list(guess, list_with_correct_word)
    if lives_in_health - damage_taken < 0:
        new_health = 0
        print(f"Congratulations, you're dead, the word was: {winning_word}")
    elif damage_taken == 0:
        return lives_in_health
    else:
        new_health = lives_in_health - damage_taken
        print(f"sorry you lost {damage_taken} HP you are at {new_health} HP")
    return new_health




juxhen = ["B","A","T"]

print(health(70, "C", juxhen))