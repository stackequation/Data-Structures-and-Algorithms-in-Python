def selectionsort(arr,q):
    for i in range(len(arr)):
        imin = i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[imin]):
                imin = j
        arr[imin],arr[i]=arr[i],arr[imin]

arr = [43,3211,234,3,4,5,33]
selectionsort(arr,6)
print(arr)
