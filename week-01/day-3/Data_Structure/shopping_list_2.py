# Shopping list 2
# Represent the following products with their prices

# Product	Amount
# Milk	1.07
# Rice	1.59
# Eggs	3.14
# Cheese	12.60
# Chicken Breasts	9.40
# Apples	2.31
# Tomato	2.58
# Potato	1.75
# Onion	1.10
# Represent Bob's shopping list
price ={
"Milk": 1.07,
"Rice":	1.59,
"Eggs": 3.14,
"Cheese":12.60,
"Chicken Breasts":9.40,
"Apples":2.31,
"Tomato":2.58,
"Potato":1.75,
"Onion": 1.10
}
# Product	Amount
# Milk	3
# Rice	2
# Eggs	2
# Cheese	1
# Chicken Breasts	4
# Apples	1
# Tomato	2
# Potato	1
# Represent Alice's shopping list

Bob ={
"Milk"	:3,
"Rice"	:2,
"Eggs"	:2,
"Cheese"	:1,
"Chicken Breasts"	:4,
"Apples"	:1,
"Tomato"	:2,
"Potato"	:1
}

# Product	Amount
# Rice	1
# Eggs	5
# Chicken Breasts	2
# Apples	1
# Tomato	10
# Create an application which solves the following problems.

Alice ={
"Rice":1,
"Eggs":5,
"Chicken Breasts":2,
"Apples":1,
"Tomato":10
}
# How much does Bob pay?
sum = 0
for i in Bob.keys():
    sum += Bob[i] * price[i]
print(sum)
# How much does Alice pay?
um = 0
for i in Alice.keys():
    sum += Alice[i] * price[i]
print(sum)

def find_items(name,key_name):
    if key_name not in name.keys():
        name[key_name] = 0
     
# Who buys more Rice?
find_items(Alice,"Rice")
find_items(Bob,"Rice")
print(max(Alice["Rice"],Bob["Rice"]))
# Who buys more Potato?
find_items(Alice,"Potato")
find_items(Bob,"Potatp")
print(max(Alice["Potato"],Bob["Potato"]))
# Who buys more different products?

# Who buys more products? (piece)/