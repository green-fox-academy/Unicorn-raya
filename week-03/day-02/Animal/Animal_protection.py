import random
class Animal:
    def __init__(self,name,healthState = False,healCost = 1):
        self.name = name 
        self.healthState = healthState
        self.healCost = healCost
    
    def heal(self):
        self.healthState = True
    
    def isAdoptable(self):
        return self.healthState
    
    def toString(self):
        if self.isAdoptable():
            return f"{self.name} is healthy, and adoptable"
        else:
            return f"{self.name} is not healthy (<{self.healCost}>€), and not adoptable"


class Cat(Animal):
    def __init__(self):
        super().__init__("Cat",False,random.randint(0,6))


class Dog(Animal):
    def __init__(self):
        super().__init__("Dog",False,random.randint(1,8))


class Parrot(Animal):
    def __init__(self):
        super().__init__("Parrot",False,random.randint(4,10))

class Animal_shelter():
    def __init__(self,animal_list = [],ap_names = []):
        self.budget = 50
        self.animal_list = animal_list
        self.adopters_names = ap_names
        self.healed_animal = []
        self.unhealed_animal = []

    def rescue(self,animal):
        self.animal_list.append(animal)
        return len(self.animal_list)
    
    def heal(self):
        healed_amount = 0
        for ani in self.animal_list:
            if not ani.isAdoptable() and self.budget > ani.healCost:
                ani.heal()
                self.budget -= ani.healCost
                healed_amount += 1
        return healed_amount
    
    def addAdopter(self,name):
        self.adopters_names.append(name)

    def findNewOwner(self):
        person_index = random.randint(0,len(self.adopters_names) - 1)
        animal_index = random.randint(0,len(self.healed_animal) - 1)
        del self.adopters_names[person_index]
        del self.healed_animal[animal_index]
    
    def earnDonation(self,money):
        self.budget += money
        return self.budget

    def splitUnheal(self):
        for ani in self.animal_list:
            if ani.isAdoptable():
                self.healed_animal.append(ani)
            else:
                self.unhealed_animal.append(ani)
    def adoptable2str(self):
        adp_list = ""
        for adp in self.healed_animal:
            adp_list += f"{adp.name} is healthy, and adoptable \n"
        return adp_list

    def unadp2str(self):
        uadp_list =  ""
        for uadp in self.unhealed_animal:
            uadp_list += f"<{uadp.name}> is not healthy ({uadp.healCost}€), and not adoptable \n"
        return uadp_list

    def toString(self):
        self.splitUnheal()
        return f"Budget: <{self.budget}>€ \n \
            There are <{len(self.animal_list)}> animal(s) and <{len(self.adopters_names)}> potential adopter(s) \n \
                {self.adoptable2str()} {self.unadp2str()}"

p1 = Parrot()
p2 = Parrot()
p3 = Parrot()

c1 = Cat()
c2 = Cat()
c3 = Cat()

d1 = Dog()
d2 = Dog()
d3 = Dog()

AL = [p1,p2,p3,c1,c2,c3,d1,d2]
Ad = ["name1","name2","name3","name4","name5"]
AS = Animal_shelter(AL,Ad)
AS.addAdopter("name6")
AS.heal()
print(AS.toString())
AS.earnDonation(20)
AS.rescue(d3)
print(AS.toString())
AS.findNewOwner()
print(AS.toString())