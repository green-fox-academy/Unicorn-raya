# What's in my bag
# We are going to represent bags using sets.

# Oliver's bag contains the following items

# Laptop
# Notebook
# Pen
# Sunglasses
# Hand sanitizer
# Ethan's bag contains the following items

# Sunglasses
# Notebook
# Phone
# Mia's bag contains the following items

# Laptop
# Sunglasses
# Hand sanitizer
# Write an application that answers the following questions

Oliver = {"Laptop", "Notebook", "Pen", "Sunglasses", "Hand sanitizer"}
Ethen = {"Sunglasses", "Notebook", "Phone"}
Mia = {"Laptop", "Sunglasses", "Hand sanitizer"}

# What are the common items in Oliver's and Ethan's bag?

print(Oliver and Ethen)
# What are the items that in Oliver's bag but not in Mia's bag?
print(Oliver ^ Mia)
# What are the common items in Oliver's, Ethan's and Mia's bag?
print(Oliver and Ethen and Mia)