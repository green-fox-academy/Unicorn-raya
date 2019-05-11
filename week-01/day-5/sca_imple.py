# Scalar multiplication
# Create a program that can multiply a matrix with a scalar.

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

def matrix_multi_scalar(mat,scalar):
    new_mat = mat
    if matrices_check(mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                new_mat[i][j] = scalar * mat[i][j] 
        return new_mat
    else:
        print("ops~ something error")
        return -1

mat_1 = [[1,2,3,4,5],[3,2,4,5,6],[1,2,3,23,4],[0,1,2,3,5]]
mat_2 = [[1,2,3,4,5],[3,2,4,5,6],[1,2,3,23,4],[3,2,4,5,6]]
mat_3 = [[1,2,3,4,5],[1,2,3,23,4]]
mat_4 = [[1,2,3,23,4],[3,2,4,5]]
scalar_1 = 0
scalar_2 = 3

print(matrix_multi_scalar(mat_1,scalar_1))
print(matrix_multi_scalar(mat_2,scalar_2))
print(matrix_multi_scalar(mat_4,scalar_1))

 
