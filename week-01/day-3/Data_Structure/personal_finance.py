# Personal finance
# We are going to represent our expenses in a list containing integers.

# Create a list with the following items.
# 500, 1000, 1250, 175, 800 and 120
# Create an application which solves the following problems.
# How much did we spend?
# Which was our greatest expense?
# Which was our cheapest spending?
# What was the average amount of our spendings?

personal_finance = [500,1000,1250,175,800,120]

print(sum(personal_finance))
print(max(personal_finance))
print(min(personal_finance))
print(round(sum(personal_finance)/len(personal_finance),2))
