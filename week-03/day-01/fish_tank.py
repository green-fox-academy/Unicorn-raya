from abc import ABCMeta, abstractmethod
class Fish:
    @abstractmethod
    def __init__(self,name ="",weight = 10,color = "",s_t_m_loss = False):
        self.name = name
        self.weight = weight
        self.color = color
        self.short_term_memory_loss = s_t_m_loss
    @abstractmethod
    def feed(self):
        pass

class Clownfish(Fish):
    def __init__(self):
        super().__init__("Clownfish",3,"stripe color")
    
    def feed(self):
        self.weight += 1
        return 1

class Tang(Fish):
    def __init__(self):
        super().__init__("Tang",True)
    
    def feed(self):
        self.weight += 1
        return 1

class Kong(Fish):
    def __init__(self):
        super().__init__("Koi")
    
    def feed(self):
        self.weight += 2
        return 2

class Aquarium():
    def __init__(self,fishes = []):
        self.fishes = fishes
    
    def add_fish(self,fish):
        self.fishes.append(fish)
    
    def eat_Fish(self):
        self.fishes = [fish for fish in self.fishes if fish.weight > 11]
    
    def feed(self,food):
        for fish in self.fishes:
            food -= fish.feed()

    def getStatus(self):
        for fish in self.fishes:
            print(f"{fish.name}, weight: {fish.weight}")
