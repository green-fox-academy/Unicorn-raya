# Addition
# Create a program that can add two matrices together.

#ensure same dimensions 
def matrices_check(mat_1,mat_2):
    mat_1_row = len(mat_1)
    mat_2_row = len(mat_2)
    if mat_1_row != mat_2_row: 
        print("dif row")
        return False
    mat_1_col = len(mat_1[0])
    for i in mat_1:
        if len(i) != mat_1_col:
            print("dif cols in mat1")
            return False
    mat_2_col = len(mat_2[0])
    for i in mat_2:
        if len(i) != mat_2_col:
            print("dif cols in mat2")
            return False
    if mat_1_col != mat_2_col:
        print("dif cols")
        return False
    return True

def matrices_add(mat_1 , mat_2):
    lst = []
    tmp = []
    if matrices_check(mat_1,mat_2):
        for row in range(len(mat_1)):
            for col in range(len(mat_1[0])):
                tmp.append(mat_1[row][col] + mat_2[row][col])
            lst.append(tmp)
            tmp = []
        return lst 
    else:
        print("ops~,please check your mat format")
        return -1 

mat_1 = [[1,2,3,4,5],[3,2,4,5,6],[1,2,3,23,4],[0,1,2,3,5]]
mat_2 = [[1,2,3,4,5],[3,2,4,5,6],[1,2,3,23,4],[3,2,4,5,6]]
mat_3 = [[1,2,3,4,5],[1,2,3,23,4]]
mat_4 = [[1,2,3,23,4],[3,2,4,5]]
test_cases=[mat_1,mat_2,mat_3,mat_4]
print(matrices_add(mat_1,mat_2)) #should print expected result
print(matrices_add(mat_1,mat_3)) # shoule print "ops~"
print(print(matrices_add(mat_1,mat_4))) #should print "illegel format"         

    
        