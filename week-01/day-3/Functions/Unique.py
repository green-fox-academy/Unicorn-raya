#  Create a function that takes a list of numbers as a parameter
#  Returns a list of numbers where every number in the list occurs only once

def unique(arr):
    lst = []
    dic = {}
    for arr_member in arr:
        if arr_member in dic.keys():
            pass
        else:
            dic[arr_member] = 1
            lst.append(arr_member)
    return lst
#  Example
print(unique([1, 11, 34, 11, 52, 61, 1, 34]))
#  should print: `[1, 11, 34, 52, 61]`

print(unique([1, 11, 34, 112, 522, 61, 1, 34]))