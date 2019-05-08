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
print(len(lst_B))
print(len(lst_A))
for i in range(len(lst_A)):
    if lst_A[i] == "Avocado":
        print(f'Avocado index is {i}')

for i in range(len(lst_B)):
    if lst_A[i] == "Durian":
        print(f'Durian index is {i}')

lst_B.extend(["Passion Fruit", "Pummelo"])

print(lst_A[2])