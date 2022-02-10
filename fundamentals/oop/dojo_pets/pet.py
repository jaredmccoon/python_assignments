class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self, sound):
        print(sound)
        return self



class firstpet(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)

pet1 = firstpet("name1", "type1", "trick1")

class secondpet(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)

pet2 = secondpet("name2", "type2", "trick2") 