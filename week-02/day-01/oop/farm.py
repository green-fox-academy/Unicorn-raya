# Farm
# Reuse your Animal class
# Create a Farm class
# it has list of Animals
# it has slots which defines the number of free places for animals
# breed() -> creates a new animal if there's place for it
# slaughter() -> removes the least hungry animal

from animal import Animal
class Farm(object):
    def __init__(self):
        self.animal_list = []
        self.capacity = 4
        animal_1 = Animal(11,41)
        animal_2 = Animal(34,31)
        animal_3 = Animal(9,54)
        self.animal_list.append(animal_1)
        self.animal_list.append(animal_2)
        self.animal_list.append(animal_3)

    def breed(self):
        if self.capacity > len(self.animal_list):
            slot = self.capacity - len(self.animal_list)
            for i in range(slot):
                self.animal_list.append(Animal())
    
    def slaughter(self):
        self.animal_list = sorted(self.animal_list,key = lambda x :x._hunger)
        self.animal_list.remove(self.animal_list[0])

    def print_current_animal(self):
        for i in self.animal_list:
            i.print_animal_properties()

farm = Farm()
farm.print_current_animal()
print("==================== 1 ===========================")
farm.breed()
farm.print_current_animal()
print("===================== 2 ==========================")
farm.slaughter()
farm.print_current_animal()