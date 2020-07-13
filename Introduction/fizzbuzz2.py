flag = False    #Setting flag so we enter the while loop
while not flag: #whilst not true
    startFrom = input("What number would you like to start with?\n") # ask user for input
    if startFrom.isnumeric(): #checks if the input is from 0-9
        startFrom = int(startFrom) # change from string input to int type
        flag = True # lifts flag to allow us to continue
    else:
        print("Listen mate, that's not a number... don't be funny") # if not numeric repeat

# Copied from above changed variable flag to flag2 and startFrom to endAt
flag2 = False
while not flag2:
    endAt = input("What number would you like to end at?\n")
    if endAt.isnumeric():
        endAt = int(endAt) + 1
        flag2 = True
        if endAt < startFrom:
            flag2 = False
            print("Please ensure end is larger than start")
    else:
        print("Listen mate, that's not a number... don't be funny")

flag3 = False    # setting flag so we enter the while loop
while not flag3:
    increment = input("What number would you like to the increment to be?\n")
    if increment.isnumeric(): # Checks if the input is from 0-9
        increment = int(increment) # Change from string input to int type
        flag3 = True #lifts flag to allow us to continue
    else:
        print("Listen mate, that's not a number... don't be funny") #if not numeric repeat

Fizz = "Fizz"
Buzz = "Buzz"
wordChange = input("Would you like to change either of the words?\n")

if len(wordChange) > 0:
    if wordChange[0].upper() == "Y":
        Fizz = input("What would you like the new 'Fizz' word to be replaced with?\n")
        Buzz = input("What would you like the new 'Buzz' word to be replaced with?\n")

new_list = []
for number in range(startFrom, endAt, increment):
    if number % 5 == 0 and number % 3 == 0:
        new_list.append(Fizz+Buzz)
    elif number % 5 == 0:
        new_list.append(Buzz)
    elif number % 3 == 0:
        new_list.append(Fizz)
    else:
        new_list.append(number)
    print(new_list[-1])