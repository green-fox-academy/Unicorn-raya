import random

class Priate():
    def __init__(self,intro_level = 0,alive = True,drink_threshold = 20):
        self.intro_level = intro_level
        self.alive = alive 
        self.drink_threshold = drink_threshold
    
    def drink_some_rum(self):
        if not self.alive:
            self.intro_level += 1

    def hows_it_going_mate(self):
        if self.intro_level < 4 and self.intro_level > 0:
            print("Pour me anudder ")
        else:
            print("R&^T^*^&(T*&T")

    #change status of idiot
    def die(self):
        self.status = False
            
    
    # throw a random number within the range of (0,3)
    # the status will be like:
    #            alive -  die
    #            die   -   alive 
    #            die   -   die
    # after battle 
    def brawl(self,another_priate):
        number = random.randint(0,2)
        if number == 1:
            #self.alive = True
            another_priate.alive = False
        elif number == 2:
            self.alive = False
            #another_priate.alive = True
        else:
            self.alive = False
            another_priate.alive = False
           