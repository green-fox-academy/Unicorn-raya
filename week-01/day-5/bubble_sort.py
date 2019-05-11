def bubble_sort(arr):
    length = len(arr)
    if length == 0:
        return -1
    else:
        for i in range(length):
            for j in range(i,length):
                if arr[i] > arr[j]:
                    arr[i],arr[j] = (arr[j],arr[i])
    return arr
             
arr = [1,2,5,7,2,11,33,23]
arr1=[]
arr2=[1]

print(bubble_sort(arr))
print(bubble_sort(arr1))
print(bubble_sort(arr2))   