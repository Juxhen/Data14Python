class Cat:

    def __init__(self):
        self._mood = 0
        self._hunger = 0
        self._energy = 0

    def sleep(self):
        if self._energy == 10:
            self._meow()
        elif 0 <= self._energy <= 9:
            self._energy += 1
        else:
            return self._energy

    def play(self):
        if self._mood == 10:
            self._meow()
        elif 0 <= self._mood <= 9:
            self._mood += 1
        else:
            return self._energy

    def feed(self):
        if self._hunger == 10:
            self._meow()
        elif 0 <= self._hunger <= 9:
            self._hunger += 1
        else:
            return self._energy

    def _meow(self):
        if self._mood == 10 and self._energy == 10 and self._hunger == 10:
            print("Meooo")
        else:
            print("I'm not 10 out of 10 in everything yet, meow")

    def get_cat_levels(self):
        print(f"Mood: {self._mood} Hunger: {self._hunger} Energy: {self._energy}")
#which methods should call meow
#which attributes should change

my_cat = Cat()
for x in range(0,10,1):
    my_cat.feed()
    my_cat.play()
    my_cat.sleep()
    my_cat.get_cat_levels()
