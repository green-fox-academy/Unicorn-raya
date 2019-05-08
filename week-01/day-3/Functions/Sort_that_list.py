#  Create a function that takes a list of numbers as parameter
#  Returns a list where the elements are sorted in ascending numerical order
#  Make a second boolean parameter, if it's `True` sort that list descending

def bubble(arr):
    arr_length = len(arr)
    if arr_length == 0:
        return -1
    for i in range(arr_length):
        for j in range(i,arr_length):
            if arr[i] > arr[j]:
                arr[i],arr[j] = (arr[j],arr[i])
    return arr 

def advanced_bubble(arr, is_descending):
    arr_length = len(arr)
    if arr_length == 0:
        return -1   

    if is_descending == False:
        bubble(arr)
    else:
        for i in range(arr_length):
            for j in range(i,arr_length):
                if arr[i] < arr[j]:
                    arr[i],arr[j] = (arr[j],arr[i])
        return arr

#  Example:
print(bubble([43, 12, 24, 9, 5]))
#  should print [5, 9, 12, 24, 34]
print(advanced_bubble([43, 12, 24, 9, 5], True))
#  should print [34, 24, 9, 5]

