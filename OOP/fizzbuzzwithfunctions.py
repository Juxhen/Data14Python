def check_start(prompt):
    start_number = input(prompt)
    if start_number.isnumeric():
       start_number = int(start_number)
    else:
        print("Please enter a valid number in number format")
        start_number = check_start(prompt)
    return start_number

start_number = check_start("Please enter a start number\n")
end_number = check_start("Please enter your end number\n")
increment = check_start("Please enter increment size\n")

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


print(fizzbuzz(start_number, end_number, increment))

