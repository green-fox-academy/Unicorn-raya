#Write a function called `sum` that returns the sum of numbers from zero to the given parameter

def sum(epoch_times):
     sum_number = 0
     for i in range(1,epoch_times + 1):
         sum_number += i
     return sum_number
print(sum(3))