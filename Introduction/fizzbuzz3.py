startFrom = 1
endAt = 100

for numbers in range(startFrom,endAt,1):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    if numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)
print(numbers)