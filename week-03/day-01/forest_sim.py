class Tree:
    def __init__(self,height = 0):
        self.height = height 
    @abs
    def irrigate(self):
        pass

    def getHeight(self):
        return self.height

class WhitebarkPine(Tree):
    def __init__(self):
        super().__init__(self)
        self.name = "WhitebarkPine"
    
    def irrigate(self):
        self.height += 2


class FoxtailPine(Tree):
    def __init__(self):
        super().__init__(self)
        self.name = "FoxtailPine"
    
    def irrigate(self):
        self.height += 1

class Lumberjack():
    def __init__(self):
        pass

    def canCut(self,tree):
        return tree.getHeight() > 4

class Forest():
    def __init__(self,treelist = []):
        self.treelist = treelist
    
    def rain(self,water_level):
        for tree in self.treelist:
            if water_level > 0:
                tree.irrigate()
                water_level -= 1
            else:
                break

    def cutTree(self,timberman):
        self.treelist = [tree for tree in self.treelist if not timberman.canCut(tree)]

    def isEmpty(self):
        return bool(len(self.treelist))

    def getStatus(self):
        for tree in self.treelist:
            print(f"There is a {tree.getHeight()} tall {tree.name} in the forest")

    

    
    


    

    

