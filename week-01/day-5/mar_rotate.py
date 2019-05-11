# Matrix rotation
# Create a program that can rotate a matrix by 90 degree.

# Extend your program to work with any multiplication of 90 degree.

def mat_rotation(mat,degree=90):
    if degree % 90 == 0:
        rotate_times = degree // 90
        rows = len(mat)
        cols = len(mat[0])
        #for row in range(rows):
        #    for col in range(cols):
        #        pass
        mat[:] = map(list,zip(*mat[::-1]))
        return mat
    else:
        print("ops~ please ensure your number could be divided by 90 *_*")


def print_2Darr_2matix(mat):
    for i in range(len(mat)):
        tmp = []
        for j in range(len(mat[0])):
            tmp.append(mat[i][j])
        print(tmp) 
mat = [[1,2,3],[4,5,6],[7,8,9]]
print_2Darr_2matix(mat)
print("===================================")
print_2Darr_2matix(mat_rotation(mat,90))


# [1,2,3]
# [4,5,6]
# [7,8,9]
# ==========
# [7,4,1]
# [8,5,2]
# [9,6,3]
