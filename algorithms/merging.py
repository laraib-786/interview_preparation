def merging(arr1,arr2,n,m):
    i=0
    j=0

    while(i<n and j<m):
        if arr1[i]<arr2[j]:
            print(arr1[i])
            i+=1
        else:
            print(arr2[j])
            j+=1
    while(i<n):
        print(arr1[i])
        i+=1
    while(j<m):
        print(arr2[j])
        j+=1

merging([10],[7],1,1)
