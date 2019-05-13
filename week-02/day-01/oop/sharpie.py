# Sharpie
# Create Sharpie class
# We should know about each sharpie their color (which should be a string), 
# width (which will be a floating point number), ink_amount (another floating point number)
# When creating one, we need to specify the color and the width
# Every sharpie is created with a default 100 as ink_amount
# We can use() the sharpie objects
# which decreases inkAmount

class Sharpie(object):
    def __init__(self,color = "None",width =0,ink_amount = 100):
        self.color = color
        self.width = float(width)
        self.ink_amount = float(ink_amount)
    def use(self):
        self.ink_amount -= 1
        return self.ink_amount

test_sharpie = Sharpie()
#print(test_sharpie.use())

