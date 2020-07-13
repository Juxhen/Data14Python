import random as r
import time as t
# import numpy as np
# from numpy.distutils.system_info import tmp


def playerHealth(Health, damage):
    Health -= damage
    if Health <= 0:
        Health = 0
    return Health

def trap(Health):
    print("you fall into a trap, uh oh!")
    damageTaken = r.randint(1, 10)
    t.sleep(2)
    Health = playerHealth(Health, damageTaken)
    print(f"you took {damageTaken} damage, your health is at {Health}")
    return Health

# def initialise(path):
#     path = input("You have spawned in Lumbridge, would you like to go\n"
#                                "'w' to go north\n"
#                                "'a' to go west\n"
#                                "'s' to go south\n"
#                                "'d' to go east\n").lower()
#     return path
#

#
# lumbridgePart1Pathway= {"North": "Trap", "East": "Trap", "West": "Trap", "South": "Clear"}
#
# pathway = np.arrange(4)  # 0, 1, 2, 3 stands for 4 paths North/South/West/East
# pathway_arrangement = np.random.shuffle(tmp).reshape(2, 2)  # reshape into a 2x2 grid
#

inputCheck1 = False
while not inputCheck1:
    character = input("Please select a character\n"
                      "'1' to play as a Mage\n"
                      "'2' to play as a Ranger\n"
                      "'3' to play as a Warrior\n")
    if character.isnumeric():
        character = int(character)
        if 0 < character < 4:
            inputCheck1 = True;
        else:
            print("Your number was out of bounds, Please enter a '1','2' or '3'")
    else:
        print("Please enter a '1','2' or '3'")

if int(character) == 1:
    print(f"Wow! Fantastic choice, Mages are magical!")
elif character == 2:
    print("Wow! Fantastic choice, Rangers are rigorous!")
else:
    print("Wow! Fantastic choice, Warriors are wicked!")
t.sleep(2)
print("We need to save the princess who is stuck at the Gnome Stronghold\n"
      "we have to first get past Lumbridge")
t.sleep(3)
characterHealth = 100  # make a dictionary so different classes have different healths
newHealth = characterHealth
lumbridgePart1 = False
damageTaken = 0
while not lumbridgePart1 and newHealth > 0:
    t.sleep(2)
    characterDirection = input("You have spawned in Lumbridge, would you like to go\n"
                               "'w' to go north\n"
                               "'a' to go west\n"
                               "'s' to go south\n"
                               "'d' to go east\n").lower()
    t.sleep(2)
    if characterDirection == "w":
        newHealth = trap(newHealth)
    elif characterDirection == "a":
        print("the west passage is clear, good job")
        lumbridgePart1 = True
        damageTaken = 0
    elif characterDirection == "s":
        newHealth = trap(newHealth)
    elif characterDirection == "d":
        newHealth = trap(newHealth)
    else:
        print("please enter a valid direction.")

if lumbridgePart1 == True:
    t.sleep(2)
    print("Congratulations you successfully passed Chapter 1 of Lumbridge")
    t.sleep(1)
    print(f"your health is at: {trap(newHealth)}")
else:
    print("GAME OVER, return to Lumbridge!")