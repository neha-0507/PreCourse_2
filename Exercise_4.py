# Python program for implementation of MergeSort 
def mergeSort(alist):
   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i = j = k = 0
       while (i < len(lefthalf) & j < len(righthalf)):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1
  
def printList(arr):
	for i in range(len(arr)):
		print(arr[i]) 
	print("")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is:")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ") 
    printList(arr) 
