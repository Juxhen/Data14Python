startInput = int(input(("What number do you want to start from?\n")))
endInput = int(input(("What number do you want to end to?\n")))
increment = int(input("What increments would you like to proceed with?\n"))
customFizz = input("What's your fizz?\n")
customBuzz = input("What's your Buzz?\n")
# theList = []
if not customFizz:
    for currentNumber in range(startInput, endInput, increment):
        if currentNumber % 3 == 0 and currentNumber % 5 == 0:
            print('FizzBuzz')
        elif currentNumber % 3 == 0:
            print('Fizz')
        elif currentNumber % 5 == 0:
            print('Buzz')
        else:
            print(currentNumber)
else:
    for currentNumber in range(startInput, endInput, increment):
        if currentNumber % 3 == 0 and currentNumber % 5 == 0:
            print(f"{customFizz}{customBuzz}")
        elif currentNumber % 3 == 0:
            print(customFizz)
        elif currentNumber % 5 == 0:
            print(customBuzz)
        else:
            print(currentNumber)