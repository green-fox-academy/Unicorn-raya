def insertion_sort(arr):
    arr_length = len(arr)
    if arr_length == 0:
        return -1
    for i in range(1,arr_length):
        tmp = arr[i]
        j = i - 1 
        while j >= 0 and tmp < arr[j]: #ensure the order 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp
    return arr


arr = [1,2,5,7,2,11,33,23]
arr1=[]
arr2=[1]

print(insertion_sort(arr))
print(insertion_sort(arr1))
print(insertion_sort(arr2))