"""
Create a list ('List A') which contains the following values
Apple, Avocado, Blueberries, Durian, Lychee
Create a new list ('List B') with the values of List A
Print out whether List A contains Durian or not
Remove Durian from List B
Add Kiwifruit to List A after the 4th element
Compare the size of List A and List B
Get the index of Avocado from List A
Get the index of Durian from List B
Add Passion Fruit and Pummelo to List B in a single statement
Print out the 3rd element from List A
"""

lst_A = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]
lst_B = lst_A[:]
if "Durian" in lst_A:
    print("Durian inside")
else:
    print("Durian is not inside")

lst_B.remove("Durian")
lst_A.insert(4,"Kiwifruit")
print(lst_B)
print(lst_A)

