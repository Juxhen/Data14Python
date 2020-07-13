def fizzbuzz(userInput, userInput2, increment):
    for x in range(userInput, userInput2, increment):
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz")
        elif x % 5 == 0:
            print("Fizz")
        elif x % 3 == 0:
            print("Buzz")
        else:
            print(x)
    return x
initialise = fizzbuzz(int(input("Please enter your starting number\n")),
                      int(input("Please enter your ending number\n")),
                      int(input("Please enter increment\n")))