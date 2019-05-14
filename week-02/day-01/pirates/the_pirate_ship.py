import random
from priates import Priate

class ship():
    def __init__(self,pirates = [],rum = 10000 ):
        self.pirates = pirates
        self.rum = rum
    
    # fill members in the ship and let head one become the captain
    def fill_ship(self):
        pirate_number = random.randint(0,10)
        index = 0
        while index < pirate_number:
            self.pirates.append(Priate())
            index += 1

    def ship_status(self):
        print(f"Captain consume {self.pirates[0].intro_level} rum")
        print(f"{len(self.pirates) - 1} crews alive")
        
    def calculate_score(self):
        return len(self.pirates) - 1 - self.pirates[0].intro_level
    
    def battle(self,another_ship):
        score_1 = self.calculate_score()
        score_2 = another_ship.calculate_score()
        if score_1 >= score_2:
            loss_crews = random.randint(0,len(another_ship.pirates))
            another_ship.pirates = another_ship.pirates[:len(another_ship.pirates)-loss_crews - 1]
            self.rum += loss_crews * 10
            return True
        else:
            loss_crews = random.randint(0,len(self.pirates))
            self.pirates = self.pirates[:len(self.pirates) - loss_crews - 1]
            another_ship.rum += loss_crews * 10
            return False



    