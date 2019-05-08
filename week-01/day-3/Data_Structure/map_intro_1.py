"""
Map introduction 1
We are going to play with maps. Feel free to use the built-in methods where possible.

Create an empty map where the keys are integers and the values are characters

Print out whether the map is empty or not

Add the following key-value pairs to the map

Key	Value
97	a
98	b
99	c
65	A
66	B
67	C
Print all the keys

Print all the values

Add value D with the key 68

Print how many key-value pairs are in the map

Print the value that is associated with key 99

Remove the key-value pair where with key 97

Print whether there is an associated value with key 100 or not

Remove all the key-value pairs
"""
dic = {}
print(dic)

key = 97
for i in range(3):
    dic[key] = chr(key)
    key += 1
key = 65
for i in range(3):
    dic[key] = chr(key)
    key += 1

print(dic.keys())
print(dic.items())

dic[68] = 'D'

print(len(dic.keys()))

del dic[97]

if 100 in dic.keys():
    print("100 is a key")
else:
    print("100 is not a key") 

dic.clear()