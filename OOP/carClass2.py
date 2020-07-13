class Trains:

    def __init__(self,):
        self.__trainspeed = 0

    def set_speed(self):
        self.__trainspeed = 0

    def get_speed(self):
        return self.__trainspeed

    def go_faster(self):
        self.__trainspeed = self.__trainspeed + 500

    def go_slower(self):
        self.__trainspeed = self.__trainspeed - 250


juxhenTrain = Trains()
juxhenTrain.go_faster()
print(juxhenTrain.get_speed())