# Main anti-diagonal mirroring
# Create a program that can mirror the given matrix across the main anti-diagonal.

def anti_diagonal_mirror(mat):
    row = len(mat)
    col = len(mat[0])
    for row_index in range(row):
        for col_index in range(row_index,col):
                mat[row_index][col_index], mat[col_index][row_index] = mat[col_index][row_index], mat[row_index][col_index]
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
print_2Darr_2matix(anti_diagonal_mirror(mat))

# Test result:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# ===================================
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]