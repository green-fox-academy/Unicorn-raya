# Product database
# We are going to represent our products in a map where the keys are strings representing the product's name and the values are numbers representing the product's price.

# Create a map with the following key-value pairs.
# Product name (key)	Price (value)
# Eggs	200
# Milk	200
# Fish	400
# Apples	150
# Bread	50
# Chicken	550
# Create an application which solves the following problems.
# How much is the fish?
# What is the most expensive product?
# What is the average price?
# How many products' price is below 300?
# Is there anything we can buy for exactly 125?
# What is the cheapest product?

dic = {
"Eggs":	"200",
"Milk":	"200",
"Fish":	"400",
"Apples": "150",
"Bread": "50",
"Chicken": "550"
}

print(dic["Fish"])
print(max(dic,key = dic.get))
print(min(dic,key = dic.get))
print(sum(int(dic[i]) for i in dic.keys()) / len(dic) )

for key in dic.keys():
    if dic[key] == "125":
        print(key)

