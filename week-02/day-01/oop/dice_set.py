import random

class DiceSet(object):

    def __init__(self):
        self.dices = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dices)):
            self.dices[i] = random.randint(1, 6)
        return self.dices

    def get_current(self, index = None):
        if index != None:
            return self.dices[index]
        else:
            return self.dices

    def reroll(self, index = None):
        if index != None:
            self.dices[index] = random.randint(1, 6)
        else:
            self.roll()
    
    def roll_all_2six(self):
        for dice_index in range(6):
            while self.dices[dice_index] != 6:
                self.reroll(dice_index)
    
    def print_all_dices(self):
        print(self.dices)

dice_set = DiceSet()
print(dice_set.get_current())
dice_set.roll()
print(dice_set.get_current())
dice_set.reroll(3)
print(dice_set.get_current(3))
print(dice_set.get_current())
print("=============================")
dice_set.roll_all_2six()
dice_set.print_all_dices()