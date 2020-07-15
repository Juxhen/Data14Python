class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.hunger = 5
        self.legs = 4
        print("I exist")

    def breathe(self):
        print("I'm breathing!")
        self.hunger += 0.1

    def eat(self):
        print("I'm eating")
        self.hunger = 0


class Mammal(Animal):

    def __init__(self, name, colour):
        super().__init__(name, 4)  # initialising arguments from super class
        self.colour = colour

    def give_birth(self):
        print("I have given birth")


class Dog(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, colour)

    def wag_tail(self):
        print("Wags Tail")
        super().breathe() # inheriting breathe method from super class Animal


# class chowchow(Dog):
#     def __init__(self, name, colour):
#         super().__init__(name, colour)
#
#     def chow_details(self):
#         print("I'm a chow chow")
#
#
# new_mammal = Mammal("Steve", )
# print(new_mammal.name)
# print(new_mammal.colour)

class Bat(Mammal):
    def __init__(self, name, colour):
        super().__init__(name, colour)
        self.legs = 2


my_bat = Bat("Bruce", "Black")
print(my_bat.legs)
