# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

length = int(input())
level = 0
tmp = ""
while level < length + 1:
    for i in range(length-level):
        tmp += " "
    for i in range(2 * level - 1):
        tmp += "*"
    for i in range(level-1):
        tmp += " "
    level += 1
    print(tmp)
    tmp = ""