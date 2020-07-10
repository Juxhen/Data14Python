# a = 5
# b = 2
# c = "Hello!"
# d = 0.25
# e = True
# f = [1,2,3]
# g = (1,2,3)
# h = {1,2,3}
#
# print(a)
# print(b)
# print(c)
#
# # How to find the type of variables
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))
# CTRL + / To comment out a block of code

# print("What is your name?")
# name = input()
# print(name)

# Use input to collect name, age and DOB from user & display them
#
# print("What is your name?")
# name = input()
# nameType = type(name)
# print("What is your age?")
# age = input()
# ageType = type(age)
# print("What is your d.o.b, format DD/MM/YY")
# dob = input()
# dobType = type(dob)
# print(name, age, dob)
# print(dobType)
#
#-----------------------------------------------------------------------
#
# name = input("What is your name?")
# age = int(input("What is your age")) #casting change one data type to another
# age = int(input("Siblings"))
# decimal = float(print("Favourite decimal"))
# animal = input("what is your fav animal")
#
# print(f"Hi {name} you're {age} and you have {siblings} your fav dec is {decimal} and your fav animal is {animal}")
#-------boolean ---------------

hw = "Hello World!"

hw.isalpha()
print(hw.islower())
print(hw.isupper())
print(hw.startswith("H"))
print(hw.endswith("!"))