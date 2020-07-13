# Function that checks if inputs are numeric and strings are string
def check_start(start_number):
    check = False
    while not check:
        if start_number.isnumeric():
            start_number = int(start_number)
            check_start = True
            return (start_number)
        else:
            print("Please enter a valid number in number format")

# Function that checks if inputs are numeric and strings are string
def check_end(end_number):
    check = False
    while not check:
        if end_number.isnumeric():
            end_number = int(end_number)
            check = True
            return (end_number)
        else:
            print("Please enter a valid number in number format")

# Function that checks if inputs are numeric and strings are string
def check_increment(increment):
    check = False
    while not check:
        if increment.isnumeric():
            start_number = int(increment)
            check = True
            return (increment)
        else:
            print("Please enter a valid number in number format")
# FizzBuzz Function Maths


def fizzbuzz(start_number, end_number, increment):
    for x in range(start_number, end_number, increment):
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz")
        elif x % 5 == 0:
            print("Fizz")
        elif x % 3 == 0:
            print("Buzz")
        else:
            print(x)
    return x

# Enter the users input
initialise_start = check_start(input("Please enter your starting number\n"))
initialise_end = check_end(input("Please enter your ending number\n"))
initialise_increment = check_increment(input("Please enter your increment number\n"))


print(fizzbuzz(initialise_start, initialise_end, initialise_increment))
