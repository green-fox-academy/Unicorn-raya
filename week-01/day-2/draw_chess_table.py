# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#

edges = int(input("input the length of edge here: "))
tmp = ""
for i in range(edges):
    if i % 2 == 0:
        for j in range(edges//2):
            tmp += " %"
        print(tmp)
        tmp = ""
    else:
        for j in range(edges//2):
            tmp += "% "
        print(tmp)       
        tmp = ""    
        
            
