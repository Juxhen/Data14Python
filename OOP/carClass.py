import random as r

class Car:

    def __init__(self, doors, model, make):
        self.__speed = 0 # super duper hidden so nobody can change it
        self.doors = doors
        self.model = model
        self.make = make

    def set_speed(self): # Set the secret speed to 0
        self.__speed = 0

    def get_speed(self): # get the secret speed
        return self.__speed

    def press_gas(self): # add 20 to speed
        if self.__speed >= 200:
            self.__speed = 200
        else:
            self.__speed = self.__speed + r.randint(10,100)

    def press_brake(self): # decrease 20 from speed
        if self.__speed <= 0:
            self.__speed = 0
        else:
            self.__speed = self.__speed - 20

juxhens_ferrari = Car("2","488","Ferrari") # Instance

# for x in range(0, 10):
#     juxhens_ferrari.press_gas()
# print(f"{juxhens_ferrari.get_speed()} MPH! oh no you crashed!")

juxhens_ferrari.press_gas()
juxhens_ferrari.press_brake()
juxhens_ferrari.press_brake()
print(juxhens_ferrari.get_speed())

#Set Max speed