# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

print("input a number: ")
store_number = 8
guess_number = int(input())
while store_number != guess_number:
    if store_number > guess_number:
        guess_number = int(input("The number is less than you guess, enter new one: "))
    else:
        guess_number = int(input("The number is larger than you guess, enter new one: "))
