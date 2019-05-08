#  Create a function that takes a number and a list of numbers as a parameter
#  Returns the indeces of the numbers in the list where the first number is part of
#  Or returns an empty list if the number is not part of any of the numbers in the list

# Example
# print(subint(1, [1, 11, 34, 52, 61]))
# should print: `[0, 1, 4]`
# print(subint(9, [1, 11, 34, 52, 61]))
# should print: '[]'

#Decompose the number and save all factors in the list and the number's length
#It is like: 53 -> [5,3,2] 
def Decomposition_factors(decom_number):
    lst = []
    decom_number_length = 0
    while decom_number:
        lst.insert(0,decom_number%10)
        decom_number //= 10
        decom_number_length += 1
    lst.append(decom_number_length)
    return lst

#print(Decomposition_factors(53))
#print(Decomposition_factors(1))

def subint(target, searched_list):
    lst = []
    index = 0
    for _target in searched_list:
        tmp_list = Decomposition_factors(_target)
        for i in tmp_list:
            if i == target:
                lst.append(index)
                break
        index += 1
    return lst

print(subint(1, [1, 11, 34, 52, 61]))
# should print: `[0, 1, 4]`
print(subint(9, [1, 11, 34, 52, 61]))
# should print: '[]'
print(subint(1, [133, 233, 2344, 52122, 63451]))
# should print: `[0, 3, 4]`
print(subint(9, [123, 1331, 3454, 512, 631]))
# should print: '[]'