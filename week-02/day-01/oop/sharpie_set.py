# Sharpie Set
# Reuse your Sharpie class
# Create SharpieSet class
# it contains a list of Sharpie
# count_usable() -> sharpie is usable if it has ink in it
# remove_trash() -> removes all unusable sharpies

from sharpie import Sharpie

class SharpieSet(object):
    def __init__(self):
        self.sharpieSet = []
        sharpie_1 = Sharpie("Yellow",5.0,19)  
        sharpie_2 = Sharpie("Yellow",5.0,13)
        sharpie_3 = Sharpie("Yellow",5.0,0)
        self.sharpieSet.append(sharpie_1)
        self.sharpieSet.append(sharpie_2)
        self.sharpieSet.append(sharpie_3)

    def count_usable(self):
        self.usable_sharpie_number = 0
        for pen in self.sharpieSet:
            if pen.ink_amount > 0:
                self.usable_sharpie_number += 1
        return self.usable_sharpie_number  
    
    def remove_trash(self):
        self.sharpieSet = []
    
    def print_sharpie_amount(self):
        print(f"current sharpie amount is: {len(self.sharpieSet)}")

sharpieSet = SharpieSet()
sharpieSet.print_sharpie_amount()
sharpieSet.remove_trash()
sharpieSet.print_sharpie_amount()