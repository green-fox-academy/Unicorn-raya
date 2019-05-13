# Animal
# Create an Animal class
# Every animal has a hunger value, which is a whole number
# Every animal has a thirst value, which is a whole number
# when creating a new animal object these values are created with the default 50 value
# Every animal can eat() which decreases their hunger by one
# Every animal can drink() which decreases their thirst by one
# Every animal can play() which increases both by one

class Animal(object):
    def __init__(self,hunger = 1,thirst = 1):
        #pass
        self._hunger = hunger
        self._thirst = thirst
    
    def eat(self):
        self._hunger -= 1
    
    def drink(self):
        self._thirst -= 1

    def play(self):
        self._hunger += 1
        self._thirst += 1

    def print_animal_properties(self):
        print(f"Animal's hunger is {self._hunger}, and Animal's thirst is {self._thirst}")

miaomiao = Animal()
#miaomiao.print_animal_properties()
miaomiao.eat()
#miaomiao.print_animal_properties()
miaomiao.drink()
#miaomiao.print_animal_properties()
miaomiao.play()
#miaomiao.print_animal_properties()
    