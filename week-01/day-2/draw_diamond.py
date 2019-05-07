# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

length = int(input()) 
level = 0
tmp = ""

if length % 2 == 0:
    length =  length // 2
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
    level -= 1
    while level > 0:
        for i in range(length-level):
            tmp += " "
        for i in range(2 * level - 1):
            tmp += "*"
        for i in range(level-1):
            tmp += " "
        level -= 1
        print(tmp)
        tmp = ""
else:
    length =  length // 2 + 1
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
    level -= 2
    while level > 0:
        for i in range(length-level):
            tmp += " "
        for i in range(2 * level - 1):
            tmp += "*"
        for i in range(level-1):
            tmp += " "
        level -= 1
        print(tmp)
        tmp = ""    