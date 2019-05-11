# Horizontal flipping
# Create a program that can horizontally flip a matrix.

def Hori_flip(mat):
    mat_length = len(mat)
    for row in range(mat_length//2):
        mat[row], mat[mat_length - 1 -row] = mat[mat_length - 1 -row],mat[row]

    return mat

def print_2Darr_2matix(mat):
    for i in range(len(mat)):
        tmp = []
        for j in range(len(mat[0])):
            tmp.append(mat[i][j])
        print(tmp) 
mat = [[1,2,3],[4,5,6],[7,8,9]]
print_2Darr_2matix(mat)
print("===================================")
print_2Darr_2matix(Hori_flip(mat))


