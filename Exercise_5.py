# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,low,high):
    i = ( low-1 )          
    pivot = arr[high]     
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 


def quickSortIterative(arr,l,h): 
  
    size = h - l + 1
    stack = [0] * (size) 
  
    top = 0
    stack[top] = l 
    top = top + 1
    stack[top] = h 

    while top >= 0: 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
        p = partition( arr, l, h ) 

        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
  
        if p+1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 

arr = [14, 32, 66, 92, 23] 
n = len(arr) 
print("Array before sorting:") 
print(arr)
quickSortIterative(arr, 0, n - 1) 
print("Array after sorting:")
print(arr)
