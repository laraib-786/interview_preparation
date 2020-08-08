arr=[19,23,43,89,12,3,4,4,5,6,7,8,9,2,3,4,12,23,34,45,34,35]

def merging(l,mid,n):
    left=arr[l:mid+1]
    right=arr[mid+1:n+1]
    i=0
    j=0
    k=l
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while(i<len(left)):
        arr[k]=left[i]
        i+=1
        k+=1
    while(j<len(right)):
        arr[k]=right[j]
        j+=1
        k+=1

def merge_sort(l,n):
    if n>l:
        mid=(n+l)//2
        merge_sort(l,mid)
        merge_sort(mid+1,n)
        merging(l,mid,n)

merge_sort(0,21)
print(arr)
