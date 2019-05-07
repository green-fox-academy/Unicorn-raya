# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs owned by the farmer
# It should print how many legs all the animals have

Chickens_number = int(input("Please input chickens' number: "))
pigs_number = int(input("Please input pigs' number: "))

Legs = Chickens_number * 2 + pigs_number * 4
print(str(Legs) + " that all the animals have")