import pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise("bark")
        return self


ninja1 = Ninja("firstname", "lastname", "treat", "food", pet.pet1)
ninja2 = Ninja("firstname", "lastname", "treat", "food", pet.pet2)

ninja1.feed().walk().bathe()

print(ninja1.pet.type)
print(ninja2.pet.name)

ninja1.pet.sleep()
print(ninja1.pet.energy)
print(ninja1.pet.health)