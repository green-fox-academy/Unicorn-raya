"""
List introduction 1
We are going to play with lists. Feel free to use the built-in methods where possible.

Create an empty list which will contain names (strings)
Print out the number of elements in the list
Add William to the list
Print out whether the list is empty or not
Add John to the list
Add Amanda to the list
Print out the number of elements in the list
Print out the 3rd element
Iterate through the list and print out each name
William
John
Amanda
Iterate through the list and print
1. William
2. John
3. Amanda
Remove the 2nd element
Iterate through the list in a reversed order and print out each name
Amanda
William
Remove all elements
"""
lst = []
print(len(lst))
lst.append("William")
print(lst)
lst.append("John")
lst.append("Amanda")
print(len(lst))
print(lst[2])
for i in lst:
    print(i)
for i in range(len(lst)):
    print(f'{i+1}. {lst[i]}')
lst.remove(lst[1])
for i in lst:
    print(i)

lst.clear()




