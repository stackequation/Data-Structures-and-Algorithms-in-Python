def partition(arr,p,q):
     pivot = arr[q]
     pindex = p
     for i in range(p,q):
             if arr[i]<=pivot:
                     arr[pindex],arr[i] = arr[i],arr[pindex]
                     pindex = pindex + 1
     arr[q] , arr[pindex] = arr[pindex] , arr[q]
     return pindex
def quicksort(arr,p,q):
     if(p<q):
             pindex = partition(arr,p,q)
             quicksort(arr,p,pindex-1)
             quicksort(arr,pindex+1,q)
arr = [56,43,22,12,32,76,55]
quicksort(arr,0,6)
print(arr)
