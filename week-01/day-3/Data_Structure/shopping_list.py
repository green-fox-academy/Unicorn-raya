# Shopping list
# We are going to represent a shopping list in a list containing strings.

# Create a list with the following items.
# Eggs, milk, fish, apples, bread and chicken
# Create an application which solves the following problems.
# Do we have milk on the list?
# Do we have bananas on the list?

def check(target, lst):
    for i in lst:
        if target == i:
            return True
    return False

lst = ["Eggs", "milk", "fish", "apples", "bread","chicken"]

print(check("milk",lst))
print(check("bananas",lst))