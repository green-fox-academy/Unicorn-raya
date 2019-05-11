def sift_up(arr,index):
    if i == 1: 
        return 
    p = i%2
    if arr[p] > arr[i]:
        return 
    else:
        arr[i],arr[p] = arr[p],arr[i]
        sift_up(arr,p)

def sift_down(arr,index):
    c = index * 2
    if arr[c] < arr[c + 1]:
        c += 1
    if arr[index] < arr[c]:
        arr[i],arr[c] = arr[c],arr[i]
        sift_down(arr,c)

def heap_sort(arr):
    pass