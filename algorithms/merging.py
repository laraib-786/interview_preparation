"""merging can be on two arrays of any size but these arrays must be sorted array.i and j are used to compare the two arrays in an efficient way so that
if some elements are left in any array so it is added in last such that all ele in merge array is sorted.
It is not necessary that i=j after execution of first loop"""



def merge(ar1,ar2,n,m):#ar1 and ar2 are sorted array
    i=0
    j=0
    merge_sorted_arr=[]
    while(i<n and j<m):
        if(ar1[i]<ar2[j]):
            merge_sorted_arr.append(ar1[i])
            i+=1
        else:
            merge_sorted_arr.append(ar2[j])
            j+=1
    for i in range(i,n):
        merge_sorted_arr.append(ar1[i])
    for j in range(j,m):
        merge_sorted_arr.append(ar2[j])
    return merge_sorted_arr
print(merge([2,3,7,9],[3,6,8,9],4,4))
print(merge([2,3,7,9,21,34,56,78,89],[12,13,23,24,45,67,78],9,7))
