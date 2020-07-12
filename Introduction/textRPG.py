import random as r
import time as t
playerCharacterChoiceIndex ={
    1: {"Type": "Mage", "Strength": "Melee", "Weakness": "Ranger"},
    2: {"Type": "Ranger", "Strength": "Mage", "Weakness": "Melee"},
    3: {"Type": "Warrior", "Strength": "Ranger", "Weakness": "Mage"},
}
playerHealthList = []
check1 = False
while not check1:
    character = input("Please select a character\n"
                    "'1' to play as a Mage\n"
                    "'2' to play as a Ranger\n"
                    "'3' to play as a Warrior\n")
    if character.isnumeric():
        character = int(character)
        if 0 < character < 4:
            check1 = True;
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
characterHealth = 100
lumbridgePart1 = False
damageTaken = 0
while not lumbridgePart1 and characterHealth - damageTaken > 0:
    t.sleep(2)
    characterDirection = input("You have spawned in Lumbridge, would you like to go\n"
          "'w' to go north\n"
          "'a' to go west\n"
          "'s' to go south\n"
          "'d' to go east\n").lower()
    t.sleep(2)
    if characterDirection == "w":
        print("you fall into a trap, uh oh!")
        damageTaken = r.randint(1,10)
        t.sleep(2)
        newHealth = characterHealth - damageTaken
        print(f"you took {damageTaken} damage, your health is at {newHealth}")
        if len(playerHealthList) == 0:
            playerHealthList.append(newHealth)
        else:
            #playerHealthList.pop()
            playerHealthList[0] = newHealth
    elif characterDirection == "a":
        print("the west passage is clear, good job")
        lumbridgePart1 = True
    elif characterDirection == "s":
        print("you fall into a trap, uh oh!")
        damageTaken = r.randint(1,10)
        t.sleep(2)
        print(f"you took {damageTaken} damage, your health is at {newHealth}")
        if len(playerHealthList) == 0:
            playerHealthList.append(newHealth)
        else:
            #playerHealthList.pop()
            playerHealthList[0] = newHealth
    elif characterDirection == "d":
        print("you fall into a trap, uh oh!")
        damageTaken = r.randint(1,10)
        t.sleep(2)
        print(f"you took {damageTaken} damage, your health is at {newHealth}")
        if len(playerHealthList) == 0:
            playerHealthList.append(newHealth)
        else:
            #playerHealthList.pop()
            playerHealthList[0] = newHealth
    else:
        print("please enter a valid direction.")
t.sleep(2)
print("Congratulations you successfully passed Chapter 1 of Lumbridge")
t.sleep(1)
print(f"your health is at: {playerHealthList[-1]}")