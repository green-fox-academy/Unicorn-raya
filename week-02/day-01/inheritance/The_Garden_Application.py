# The Garden Application
# The task is to create a garden application, so in your main method you should create a garden with flowers and trees. The program should demonstrate an example garden with two flowers (yellow and blue) and two trees (purple and orange). In the example after creating them you should show the user, how the garden looks like. After that the program should water the garden twice, first with the amount of 40 then with 70. And after every watering the user should see the state of the garden as you can see in the output.

# The output should look like this:

# The yellow Flower needs water
# The blue Flower needs water
# The purple Tree needs water
# The orange Tree needs water

# Watering with 40
# The yellow Flower doesnt need water
# The blue Flower doesnt need water
# The purple Tree needs water
# The orange Tree needs water

# Watering with 70
# The yellow Flower doesnt need water
# The blue Flower doesnt need water
# The purple Tree doesnt need water
# The orange Tree doesnt need water
# Information on the elements
# The Garden
# is able to hold unlimited amount of flowers or trees
# when watering it should only water those what needs water with equally divided amount amongst them
# eg. watering with 40 and 4 of them need water then each gets watered with 10
# The Flower
# needs water if its current water amount is less then 5
# when watering it the flower can only absorb the 75% of the water
# eg. watering with 10 the flower's amount of water should only increase with 7.5
# The Tree
# needs water if its current water amount is less then 10
# when watering it the tree can only absorb the 40% of the water
# eg. watering with 10 the tree's amount of water should only increase with 4


class Flower(object):
    def __init__(self,name,water):
        self.water = water
        self.name = name

    def water_level_status(self):
        if self.water < 5:
            print(f"the {self.name} flower needs water")
        else:
            print(f"The {self.name} Flower doesnt need water")

    def absorb(self,water):
        self.water += water * 0.75

class Tree(object):
    def __init__(self,name,water):
        self.water = water
        self.name = name

    # def is_water_needed(self):
    #     return self.water < 10

    def water_level_status(self):
        if self.water < 10:
            print(f"the {self.name} tree needs water")
        else:
            print(f"The {self.name} tree doesnt need water")

    def absorb(self,water):
        self.water += water * 0.4

class Garden(object):
    def __init__(self,water_level,flowers = [],trees = []):
        self.water_level = water_level
        self.flowers = flowers
        self.trees = trees

    def element_init(self):
        self.flowers.append(Flower("yellow",0))
        self.flowers.append(Flower("blue",0))
        self.trees.append(Tree("purple",0))
        self.trees.append(Tree("orange",0))

    def water_level_status(self):
        for fl in self.flowers:
            fl.water_level_status()
        for tr in self.trees:
            tr.water_level_status() 
    
    def watering(self,water_level):
        water = water_level/(len(self.trees)+len(self.flowers))   
        for fl in self.flowers:
            fl.absorb(water)
        for tr in self.trees:
            tr.absorb(water)

g = Garden(0)
g.element_init()
g.water_level_status()

g.watering(40)
g.water_level_status()

g.watering(70)
g.water_level_status()

    


    