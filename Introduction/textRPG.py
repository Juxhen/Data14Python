playerCharacterChoiceIndex ={
    1: {"Type": "Mage", "Strength": "Melee", "Weakness": "Ranger"},
    2: {"Type": "Ranger", "Strength": "Mage", "Weakness": "Melee"},
    3: {"Type": "Warrior", "Strength": "Ranger", "Weakness": "Mage"},
}
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

