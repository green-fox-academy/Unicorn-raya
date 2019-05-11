# matrix multi
# check mat format
def matrices_check(mat_1):
    mat_1_col = len(mat_1[0])
    for i in mat_1:
        if len(i) != mat_1_col:
            print("dif cols in mat1")
            return False
    return True

def mat_multi_format_check(mat_1,mat_2):
    if matrices_check(mat_1) and matrices_check(mat_2):
        mat_1_row = len(mat_1)
        mat_1_col = len(mat_1[0])
        mat_2_row = len(mat_2)
        mat_2_col = len(mat_2[0])
        if mat_1_col == mat_2_row and mat_2_col == mat_1_row:
            return True
    return False

def mat_multi(mat_1,mat_2):
    if mat_multi_format_check(mat_1,mat_2):
       rowA = len(mat_1)
       colA = len(mat_1[0])
       #rowB = len(mat_2)
       colB = len(mat_2[0])
       new_mat = [rowA *[0] for i in range(colB)]
       for i in range(rowA):
           for j in range(colB):
               for k in range(colA):
                   new_mat[i][j] += mat_1[i][k] * mat_2[k][j]
			
       return new_mat
    else:
        print("ops~ format error")
mat_1 = [[1,2,3],[3,2,4],[1,2,3],[0,1,2]]
mat_2 = [[1,2,3,4],[3,2,4,5],[1,2,3,23]]
mat_3 = [[1,2,3,4,5],[1,2,3,23,4]]

print(mat_multi(mat_1,mat_2))
print(mat_multi(mat_1,mat_3))




