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
tmp = ""

for i in range(length+1):
    for j in range(i):
        tmp += "*"
    print(tmp + '\n')
    tmp = ""