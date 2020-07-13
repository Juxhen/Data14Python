# class GoodDog:
#
#     animal_type = "canine" # Attribute (variable)
#
#     def bark(self): # Method (Function inside classes)
#         return "Woof!"
#
#
# simba = GoodDog() # Created instance of class (an Object)
# print(simba.animal_type)
# print(simba.bark())
#
# fido = GoodDog()
# lassie = GoodDog()
#
# fido.animal_type = "Bird"
# print(simba.animal_type)
#
# GoodDog.animal_type = "arachnid"
#
# print(lassie.animal_type)


class Dog:

    def __init__(self, name, breed, colour): # Initialisation
        self.name = name
        self.legs = 4
        self.animal_kind = "canine"
        self.breed = breed
        self.colour = colour
        self._secret = "Dogs like chocolate" # Private Variable - if you place an underscore infront of the word its secret the IDE thinks its hidden
        self.__secret = "Dogs like chocolate" # Completely hides the variable but you can call it within the class

    def bark(self):
        return "WOOF!"

    def greeting(self):
        return f"Hello I am {self.name} I am a {self.breed} and my fur is nice and {self.colour}"

    def get_secret(self): # GETTER
        return self.__secret

    def set_secret(self, secret): # SETTER
        self.__secret = secret


juxhens_dog = Dog("Simba","Chow Chow", "Golden") # Instantiation


print(juxhens_dog.greeting())
# whatever is in the init method will not be changed by chaging outside variables

#using getters and setters

print(juxhens_dog.get_secret())
juxhens_dog.set_secret("I like chickem")
print(juxhens_dog.get_secret())
