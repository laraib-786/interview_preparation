
#arr=[6,5,8,9,3,10,15,12,16,1000]
arr=[3,2,6,43,9,12,13,21,34,14,18,19,1000]
def partition(l,h):
    pivot=arr[l]
    i=l
    j=h
    while(i<j):
        i+=1# just to start from i=1 index because 0th element is pivot element each time
        while(arr[i]<=pivot):
            i+=1
        j-=1# just to ignore sorted jth position. so we add last infinity element to maintain this expression
        while(arr[j]>pivot):
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if(arr[l]>arr[j]):
        arr[j],arr[l]=arr[l],arr[j]
    return j
def quick_sort(l,h):
    if (l<h):
        pi=partition(l,h)
        quick_sort(l,pi)
        quick_sort(pi+1,h)
quick_sort(0,12)
print(arr)
