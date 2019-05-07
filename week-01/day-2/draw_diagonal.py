# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was

edge = int(input())
index = 0
#print(edge * "%")
tmp = ""
while index < edge - 2:
    for i in range(edge):
        if i == 0 or i == edge - 1 or i - 1 == index:
            tmp += "%"
        else:
            tmp += " "
    index += 1
    print(tmp)
    tmp = ""
#print(edge * "%")