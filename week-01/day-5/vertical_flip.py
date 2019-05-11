# Vertical flipping
# Create a program that can vertically flip a matrix.

def matrices_check(mat_1):
    # mat_1_row = len(mat_1)
    # mat_2_row = len(mat_2)
    # if mat_1_row != mat_2_row: 
    #     print("dif row")
    #     return False
    mat_1_col = len(mat_1[0])
    for i in mat_1:
        if len(i) != mat_1_col:
            print("dif cols in mat1")
            return False
    # mat_2_col = len(mat_2[0])
    # for i in mat_2:
    #     if len(i) != mat_2_col:
    #         print("dif cols in mat2")
    #         return False
    # if mat_1_col != mat_2_col:
    #     print("dif cols")
    #     return False
    return True

def mat_vartical_flip(mat):
    row = len(mat)
    col = len(mat[0])
    for row_index in range(row):
        for col_index in range(col//2):
            mat[row_index][col_index],mat[row_index][row-1-col_index] = mat[row_index][row-1-col_index],mat[row_index][col_index]
    return mat

mat1 = [[1,2,3,4,5],[5,4,3,2,1]]
mat2 =[[1,2,3,4],[4,3,2,1]]

print(mat_vartical_flip(mat1))

print(mat_vartical_flip(mat2))