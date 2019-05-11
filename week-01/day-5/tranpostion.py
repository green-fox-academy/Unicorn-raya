# Transposition
# Create a program that calculates the transposition of a matrix.
def matrices_check(mat_1):
    mat_1_col = len(mat_1[0])
    for i in mat_1:
        if len(i) != mat_1_col:
            print("dif cols in mat1")
            return False
    return True

def transposition(mat_1):
    if matrices_check(mat_1):
        new_mat = []
        tmp = []
        for cols in range(len(mat_1[0])):
            for rows in range(len(mat_1)):
                tmp.append(mat_1[rows][cols])
            new_mat.append(tmp)
            tmp=[]
        return new_mat
    else:
        return -1

mat = [[2,3,3,4],[1,2,3,5],[3,4,5,5]]
print(transposition(mat))