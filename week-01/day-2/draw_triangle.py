# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was


length = int(input())

for i in range(length):
    print('\n')
    for j in range(i):
        print("*")
    