class Hero:
    def __init__(self,name = "",motivation = 0):
        self.name = name
        self.motivation = motivation

    def getMotivationLevel(self):
        if self.motivation > 40:
            return 2
        elif self.motivation < 25:
            return 0
        else:
            return 1

    def punch(self,bad_man):
        if self.motivation > 1:
            return self.motivation/1.5
        else:
            print("Exhaused")
    
    def bePunched(self,damage):
        self.motivation -= (damage/self.motivation)

    def toString(self):
        if self.getMotivationLevel() == 0:
            return f"{self.name} is not motivated anymore."
        elif self.getMotivationLevel() == 1:
            return f"{self.name} is motivated."
        else:
            return f"{self.name} is well motivated."

class DCHero(Hero):
    def __init__(self,DCname):
        super().__init__(DCname,45)

    def hit(self,evilman):
        if not isinstance(evilman,DCHero):
            print("Another universal hero...")
        else:
            self.punch(evilman)

class MarvelHero(Hero):
    def __init__(self,MVname):
        super().__init__(MVname,40)

    def hit(self,evilman):
        if not isinstance(evilman,MarvelHero):
            print("Another universal hero...")
        else:
            self.punch(evilman)

