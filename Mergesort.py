def mergesort(arr):
   
  if len(arr) > 1:
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left)
    mergesort(right)
    i=0
    j=0
    k=0
    while i<len(left) and j<len(right) :
        if left[i]<=right[j]:
            arr[k]=left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
        k=k+1
    while i<len(left):
        arr[k]=left[i];
        i=i+1
        k=k+1
    while j<len(right):
        arr[k]=right[j];
        j=j+1
        k=k+1
arr = [56,67,23,12,34,55]
mergesort(arr)
print(arr)
            
        
