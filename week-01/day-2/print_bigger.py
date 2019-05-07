# Write a program that asks for two numbers and prints the bigger one
total_numbers = 2
bigger_one = -999999
while total_numbers:
    total_numbers -=1
    tmp = int(input())
    if bigger_one < tmp:
        bigger_one = tmp

print(f'the bigger one is: {bigger_one}')
